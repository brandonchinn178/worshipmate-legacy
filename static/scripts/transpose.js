Number.prototype.mod = function(n) {
    return ((this % n) + n) % n;
};

$(document).ready(function() {
    setScale();
    shiftChords(0);
    setupTranspose();
});

function setScale() {
    var scaleRow = document.getElementById("scale");
    for (i = -6; i < 6; i++) {
        var scaleNode = document.createElement("td");
        scaleNode.innerHTML = (i > 0 ? "+" : "") + i;
        scaleRow.appendChild(scaleNode);
    }
}

function shiftChords(base) {
    const chords = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B'];
    var chordRow = document.getElementById("chords");
    var start = (base + 6) % chords.length;
    var val = start;

    $.fn.setClick = function(base) {
        this.click(function() {
            $("#chords").empty();
            shiftChords(base);
        });
        return this;
    };

    for (var i = 0; i < chords.length; i++, val++) {
        val = val == chords.length ? 0 : val;
        var chordNode = document.createElement("td");
        chordNode.innerHTML = chords[val];
        chordNode.id = "chord" + val;
        chordRow.appendChild(chordNode);
        $("#chord"+val).setClick(val);
    }
}

function setupTranspose() {
    const defaultVal = 0;
    var select = document.getElementById("change");
    for (i = -6; i < 6; i++) {
        var option = document.createElement("option");
        option.innerHTML = i;
        if (i == defaultVal) {
            option.selected = "selected";
        }
        select.appendChild(option);
    }

    $("#submit").click(transposeChords);
}

function transposeChords() {
    if ($("chords").value == "") {
        return;
    }

    const chords = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#'];

    function extractChords() {
        var parsed = $("#old-chords").val().replace(/[^\w\d\/#]/g," ").split(" ");
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
            if (typeof dict[chord] === "undefined") {
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
        Element.prototype.createChild = function(type, inner) {
            var element = document.createElement(type);
            element.innerHTML = inner;
            this.appendChild(element);
        }

        $("#result").empty();
        var table = document.getElementById("result");
        var firstRow = document.createElement("tr");


        firstRow.createChild("th", "Original");
        firstRow.createChild("th", "");
        firstRow.createChild("th", "Transposed");

        table.appendChild(firstRow);

        for (oldChord in chordDict) {
            var newChord = chordDict[oldChord];
            var row = document.createElement("tr");
            row.createChild("td", oldChord);
            row.createChild("td", "&rarr;");
            row.createChild("td", newChord=="NaN"? "Not a valid chord" : newChord);

            table.appendChild(row);
        }
    }

    var oldChords = extractChords();
    var diff = parseInt($("#change").val())
    var chordDict = transposeAndPair(oldChords, diff);
    changeHTML(chordDict);
}