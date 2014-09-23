$(document).ready(function() {
    $('#song-table')
        .tablesorter({
            headers: {
                2: { sorter: false },
                3: { sorter: false }
            }
        })
        .bind('sortEnd', reColor);

    setUpTags();
});

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
    var songs = $(".song");

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