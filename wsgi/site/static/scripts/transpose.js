Number.prototype.mod = function(n) {
    return ((this % n) + n) % n;
};
const chords = ['F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F'];
var middle = 6;

$(document).ready(function() {
    setScale();
    setupTranspose();
});

function setScale() {
    var scale = $("#scale");
    for (i = -6; i <= 6; i++) {
        // add a + sign to positive numbers
        var num = (i > 0 ? "+" : "") + i;
        scale.append("<div>" + num + "</div>");
    }

    function setClick() {
        var index = chords.indexOf(this.textContent);
        var diff = index - middle;
        shiftChords(diff);
    }

    var chordRow = $("#chords");
    chords.forEach(function(chord, i, array) {
        $("<div class='chord'></div>")
            .text(chord)
            .click(setClick)
            .appendTo(chordRow);
    });

    $("<div class='chord'></div>")
        .text(chords[0])
        .click(setClick)
        .appendTo(chordRow);
};

function shiftChords(diff) {
    if (diff == 0) return;

    var last = $(".chord:last-child");
    var row = $("#chords");
    if (diff < 0) {
        $(".chord:gt(" + (diff - 2) + ")").prependTo(row);
    } else {
        $(".chord:lt(" + diff + ")").appendTo(row);
    }
    row.append(last);
    last.text(row.children()[0].textContent);
    middle = chords.indexOf(row.children()[6].textContent);
}

function setupTranspose() {
    const defaultVal = 0;
    var select = $(".input-change")[0];
    for (i = -6; i < 6; i++) {
        var option = document.createElement("option");
        option.innerHTML = i;
        if (i == defaultVal) {
            option.selected = "selected";
        }
        select.appendChild(option);
    }

    $(".app-container .input-change").change(transposeChords);
    $(".app-container .input-chords").change(transposeChords);
}

function transposeChords() {
    if ($(".input-chords")[0].value === "") {
        return;
    }

    const chords = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#'];

    function extractChords() {
        var parsed = $(".input-chords").val().replace(/[^\w\d\/#]/g," ").split(" ");
        for (i = 0; i < parsed.length; i++) {
            if (parsed[i] === "") {
                parsed.splice(i--, 1);
            }
        }
        return parsed;
    }

    function transposeAndPair(oldChords, diff) {
        var dict = {};
        for (i = 0; i < oldChords.length; i++) {
            var chord = oldChords[i];
            if (!(chord in dict)) {
                dict[chord] = transpose(chord, diff);
            }
        }
        return dict;
    }

    function transpose(chord, diff, startIndex) {
        String.prototype.replaceWith = function(index, str) {
            return this.slice(0,index) + str + this.slice(index+1);
        };

        var startIndex = typeof startIndex === "undefined" ? 0 : startIndex;
        var oldIndex = chords.indexOf(chord[startIndex].toUpperCase());
        var nextIndex = startIndex + 1;

        if (oldIndex == -1) {
            return "NaN";
        }

        if (chord.length > nextIndex && chord[nextIndex].search(/(#|b)/) != -1) {
            oldIndex += chord[nextIndex] == "#" ? 1 : -1;
            chord = chord.replaceWith(nextIndex, "");
        }

        chord = chord.replaceWith(startIndex, chords[(oldIndex + diff).mod(12)]);
        slash = chord.indexOf("/", startIndex);
        return slash == -1 ? chord : transpose(chord, diff, slash + 1);
    }

    function changeHTML(chordDict) {
        $(".app-result").empty();
        var row = "<tr><th>Original</th><th></th><th>Transposed</th></tr>";
        $(".app-result").append(row);

        for (oldChord in chordDict) {
            var newChord = chordDict[oldChord];
            if (newChord === "NaN") {
                newChord = "Not a valid chord";
            }
            row = "<tr><td>" + oldChord + "</td><td>&rarr;</td><td>" + newChord + "</td></tr>";
            $(".app-result").append(row);
        }
    }

    var oldChords = extractChords();
    var diff = parseInt($(".input-change").val())
    var chordDict = transposeAndPair(oldChords, diff);
    changeHTML(chordDict);
}