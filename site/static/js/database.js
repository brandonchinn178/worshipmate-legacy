var HEADER_HEIGHT, FILTER_BAR_HEIGHT, table;
var filters = [];

$(document).ready(function() {
    var options = {
        dom: "t",
        paging: false,
        order: [],
        columnDefs: [
            {
                targets: 2,
                orderable: false,
            }
        ],
    };

    table = $(".songs-table").DataTable(options);
    HEADER_HEIGHT = $("header").outerHeight();
    FILTER_BAR_HEIGHT = $(".filter-bar").outerHeight();

    // set up scroll
    $(window)
        .scroll(function() {
            // header is showing
            if ($(this).scrollTop() < HEADER_HEIGHT) {
                $(".filter-bar").removeClass("sticky");
            } else {
                $(".filter-bar").addClass("sticky");
            }
        })
        // trigger to initialize
        .scroll();

    $(".songs-table")
        .find(".themes a, .speed a")
        .click(function() {
            addFilter($(this).text());
            return false;
        });

    if (history.state !== null) {
        $.each(history.state, function(i, val) {
            addFilter(val);
        });
    }
});

var addFilter = function(tag) {
    if ($.inArray(tag, filters) !== -1) {
        return;
    }

    // do filter
    $(".songs-table tbody tr")
        .hide()
        .each(function() {
            var themes = $(this)
                .find(".themes")
                .text()
                .split(", ");
            var passesFilter = filters.every(function(tag) {
                return $.inArray(tag, themes);
            });
            if (passesFilter) {
                $(this).show();
            }
        });

    // add to filters list
    var item = $("<li>");
    $("<a>")
        .text(tag)
        .attr("href", "#")
        .appendTo(item)
        .click(function() {
            removeFilter($(this).text());
            return false;
        });

    filters.push(tag);
    $(".filters-list").append(item);

    if (filters.length === 1) {
        $(".filter-bar").show();
        $(".content").css("margin-top", FILTER_BAR_HEIGHT);
    }

    updateState();
};

var removeFilter = function(tag) {
    filters.splice(filters.indexOf(tag), 1);
    $(".filters-list a").each(function() {
        if ($(this).text() === tag) {
            $(this).parent().remove();
        }
    });

    if (filters.length === 0) {
        $(".filter-bar").hide();
        $(".content").css("margin-top", "");
    }

    updateState();
};

/**
 * When filtering, always save state so user can navigate back to same state
 */
var updateState = function() {
    if (window.location.hash === "") {
        window.history.pushState(filters, "", "#filter");
    } else {
        window.history.replaceState(filters, "");
    }
};
