const NDASH = "\u2013";
const UPARR = "\u2191";
const DOWNARR = "\u2193";
var songs;
var parent;
var current = "title";

$(document).ready(function() {
    songs = document.getElementById("songs").getElementsByClassName("song");
    parent = songs[0].parentNode;

    const IDs = ["title", "artist"];
    for (var i = 0; i < IDs.length; i++) {
        var id = IDs[i];
        $("#"+id).click(function(_id) {
            return function() {
                sortTable(_id);
            };
        }(id));
        $("#"+id).css("cursor", "pointer");
    }
    getSymbolNode(current).textContent = UPARR;
    sortBy("title");

    setUpTags();
});

function sortTable(id) {
    var symbolNode = getSymbolNode(id);

    if (id === current) {
        var symbol = symbolNode.textContent === UPARR ? DOWNARR : UPARR;
        symbolNode.textContent = symbol;
        flip();
    } else {
        getSymbolNode(current).textContent = NDASH;
        symbolNode.textContent = UPARR;
        current = id;
        sortBy(id);
    }
}

function sortBy(sortId) {
    function isCorrectOrder(s1, s2) {
        return s1.children[sortColumn].textContent <=
            s2.children[sortColumn].textContent;
    }

    var sortColumn = sortId == "title" ? 0 : 1;
    for (var i = 1; i < songs.length; i++) {
        for (var j = 0; j < i; j++) {
            if (!isCorrectOrder(songs[j], songs[i])) {
                parent.insertBefore(songs[i], songs[j]);
                break;
            }
        }
    }
}

function flip() {
    for (var i = 1; i < songs.length; i++) {
        parent.insertBefore(songs[i], songs[0]);
    }
}

function getSymbolNode(id) {
    return document.getElementById(id).querySelector(".sort");
}

function setUpTags() {
    function setClick(tag, column) {
        return function() {
            filter(tag, column);
        }
    }
    for (var i = 0; i < songs.length; i++) {
        var themeColumn = songs[i].children[2];
        var speedColumn = songs[i].children[3];
        var themes = themeColumn.textContent.split(", ");
        themeColumn.textContent = "";
        for (var j = 0; j < themes.length; j++) {
            var button = document.createElement("button");
            button.textContent = themes[j];
            button.onclick = setClick(button.textContent, 2)
            themeColumn.appendChild(button);
        }

        var speed = document.createElement("button");
        speed.textContent = speedColumn.textContent;
        speed.onclick = setClick(speed.textContent, 3);
        speedColumn.textContent = "";
        speedColumn.appendChild(speed);

        songs[i].contains = function(row) {
            return function(tag, column) {
                var buttons = row.querySelectorAll("button");
                for (var i = 0; i < buttons.length; i++) {
                    if (buttons[i].textContent === tag) {
                        return true;
                    }
                }
                return false;
            };
        }(songs[i]);
    }
}

var filtered = {
    "tags": [],
    "songs": [],
};

function filter(tag, column) {
    if (filtered["tags"].indexOf(tag) != -1) {
        var buttons = document.getElementById("filters").children;
        for (var i = 0; i < buttons.length; i++) {
            if (buttons[i].textContent === tag) {
                buttons[i].click();
                return;
            }
        }
        console.error("Something went wrong");
    }

    filtered["tags"].push(tag);

    for (var i = 0; i < songs.length; i++) {
        var song = songs[i];
        if (!song.contains(tag, column)) {
            var removed = song.parentNode.removeChild(song);
            filtered["songs"].push(removed);
            i--;
        }
    }
    var button = document.createElement("button");
    button.textContent = tag;
    button.onclick = function() {
        return function() {
            this.parentNode.removeChild(this);
            unfilter(tag, column);
        };
    }(tag, column);
    document.getElementById("filters").appendChild(button);
}

function unfilter(tag, column) {
    var alltags = filtered["tags"];
    var allsongs = filtered["songs"];

    alltags.splice(alltags.indexOf(tag), 1);
    for (var i = 0; i < allsongs.length; i++) {
        var skip = false;
        for (var j = 0; j < alltags.length; j++) {
            if (!allsongs[i].contains(alltags[j])) {
                skip = true;
                break;
            }
        }

        if (!skip) {
            parent.appendChild(allsongs[i]);
            allsongs.splice(i--, 1);
        }
    }
    sortBy(current);
}