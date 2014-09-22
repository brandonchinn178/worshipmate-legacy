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
    //sortBy("title");

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
    function setClick(tag) {
        return function() {
            var tags = $(".filter").select2("val");
            if (tags.indexOf(tag) == -1) {
                tags.push(tag);
                $(".filter").select2("val", tags).trigger("addTag", [tag]);
            } else {
                tags.splice(tags.indexOf(tag), 1);
                $(".filter").select2("val", tags).trigger("removeTag", [tag])
            }
        };
    };

    var tags = new Set();

    for (var i = 0; i < songs.length; i++) {
        var themeColumn = songs[i].children[2];
        var speedColumn = songs[i].children[3];
        var themes = themeColumn.textContent.split(", ");
        themeColumn.textContent = "";
        for (var j = 0; j < themes.length; j++) {
            var button = document.createElement("button");
            button.textContent = themes[j];
            button.onclick = setClick(themes[j]);
            themeColumn.appendChild(button);

            tags.add(themes[j]);
        }

        var speed = document.createElement("button");
        speed.textContent = speedColumn.textContent;
        speedColumn.textContent = "";
        speed.onclick = setClick(speed.textContent);
        speedColumn.appendChild(speed);
    }

    var tagArray = ["Fast", "Slow", "Fast/Slow"];
    tags.forEach(function(tag) {
        tagArray.push(tag);
    });

    tagArray.sort().forEach(function(tag) {
        var option = document.createElement("option");
        option.text = tag;
        $(".filter").append(option);
    });

    $(".filter")
        .select2({
            placeholder: "Filter by...",
            formatNoMatches: "No tags found"
        })
        .change(function(evt, params) {
            if (evt.added) {
                $(".filter").trigger("addTag", [evt.added.text]);
            } else {
                $(".filter").trigger("removeTag", [evt.removed.text]);
            }
        })
        .on("addTag", function(evt, params) {
            filter(params);
        })
        .on("removeTag", function(evt, params) {
            unfilter(params);
        });
}

function filter(tag) {
    var songs = $(".song").not(":hidden");

    function isFiltered(buttons) {
        for (var i = 0; i < buttons.length; i++) {
            if (buttons[i].textContent == tag) {
                return false;
            }
        }
        return true;
    }

    for (var i = 0; i < songs.length; i++) {
        if (isFiltered(songs[i].querySelectorAll("button"))) {
            songs[i].style.display = "none";
        }
    }
    reColor();
}

function unfilter(tag) {
    var tags = $(".filter option:selected").toArray().map(function(option) {
        return option.textContent;
    });
    var songs = $(".song:hidden");

    function isShowable(buttons) {
        var label = [];
        for (var i = 0; i < buttons.length; i++) {
            label.push(buttons[i].textContent);
        }

        for (var i = 0; i < tags.length; i++) {
            if (label.indexOf(tags[i]) == -1) {
                return false;
            }
        }
        return true;
    }

    for (var i = 0; i < songs.length; i++) {
        if (isShowable(songs[i].querySelectorAll("button"))) {
            songs[i].style.display = "";
        }
    }
    
    reColor();
}

function reColor() { 
    // odd rows that aren't hidden should have the "odd" class
    $(".song:not(:hidden)").filter(":odd").removeClass("even").addClass("odd");
    // even rows that aren't hidden should have the "even" class
    $(".song:not(:hidden)").filter(":even").removeClass("odd").addClass("even");
}