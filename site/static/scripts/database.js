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

    $(".song").each(function(index) {
        var themeColumn = $("td:eq(2)", this);
        var themes = themeColumn.text().split(", ");
        themeColumn.text("");

        themes.forEach(function(theme) {
            $("<button>" + theme + "</button>")
                .click(setClick(theme))
                .appendTo(themeColumn);

            tags.add(theme);
        });

        var speedColumn = $("td:eq(3)", this);
        var speed = speedColumn.text();
        speedColumn.text("");
        $("<button>" + speed + "</button>")
            .click(setClick(speed))
            .appendTo(speedColumn);
    });

    var tagArray = ["Fast", "Slow", "Fast/Slow"];
    tags.forEach(function(tag) {
        tagArray.push(tag);
    });

    tagArray.sort().forEach(function(tag) {
        $("<option>" + tag + "</option>").appendTo(".filter");
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
    function isFiltered(buttons) {
        for (var i = 0; i < buttons.length; i++) {
            if (buttons[i].textContent == tag) {
                return false;
            }
        }
        return true;
    }

    $(".song").not(":hidden").each(function(index) {
        if (isFiltered($("button", this))) {
            this.style.display = "none";
        }
    })

    reColor();
}

function unfilter(tag) {
    var tags = $(".filter option:selected").toArray().map(function(option) {
        return option.textContent;
    });

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

    $(".song:hidden").each(function(index) {
        if (isShowable($("button", this))) {
            this.style.display = "";
        }
    })

    reColor();
}

function reColor() { 
    // odd rows that aren't hidden should have the "odd" class
    $(".song:not(:hidden)").filter(":odd").removeClass("even").addClass("odd");
    // even rows that aren't hidden should have the "even" class
    $(".song:not(:hidden)").filter(":even").removeClass("odd").addClass("even");
}