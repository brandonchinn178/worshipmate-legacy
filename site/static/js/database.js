var HEADER_HEIGHT, FILTER_BAR_HEIGHT, table;
window.state = {
    filters: [],
    search: "",
};

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
        language: {
            zeroRecords: "No songs found",
        },
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

    // add filter interactions
    $(".songs-table")
        .find(".themes a, .speed a")
        .click(function() {
            addFilter($(this).text());
            return false;
        });

    // set up search bar
    $(".search-bar input").keyup(function() {
        updateSearch($(this).val());
    });

    // update state
    if (window.history.state !== null) {
        applyState();
    }
});

/** 
 * Custom filtering function which filters rows based on the selected tags
 * after searching for text
 *
 * Ex. https://datatables.net/examples/plug-ins/range_filtering.html
 */
$.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {
    var tags = data[2].split(", ");
    var speed = data[3];
    tags.push(speed);

    // Fast/Slow also acts as both Fast and Slow
    if (speed === "Fast/Slow") {
        tags.push("Fast");
        tags.push("Slow");
    }

    var filters = window.state.filters;
    for (var i = 0; i < filters.length; i++) {
        if (tags.indexOf(filters[i]) === -1) {
            return false;
        }
    }
    return true;
});

/**
 * Adds filter to the state and the filter bar
 */
var addFilter = function(tag) {
    // if tag already being filtered, remove instead
    if (window.state.filters.indexOf(tag) !== -1) {
        removeFilter(tag);
        return;
    }

    // update filter list
    window.state.filters.push(tag);

    // update filter bar
    var item = $("<li>");
    $("<a>")
        .text(tag)
        .attr("href", "#")
        .appendTo(item)
        .click(function() {
            removeFilter($(this).text());
            return false;
        });
    $(".filters-list").append(item);

    if (window.state.filters.length === 1) {
        $(".filter-bar").show();
        $(".content").css("margin-top", FILTER_BAR_HEIGHT);
    }

    doFilter();
};

/**
 * Removes filter from state and the filter bar
 */
var removeFilter = function(tag) {
    // update filter list
    var index = window.state.filters.indexOf(tag);
    window.state.filters.splice(index, 1);

    // update filter bar
    $(".filters-list a")
        .filter(function() {
            return $(this).text() === tag;
        })
        .parent().remove();

    if (window.state.filters.length === 0) {
        $(".filter-bar").hide();
        $(".content").css("margin-top", "");
    }

    doFilter();
};

/**
 * Updates search query in state and filter bar
 */
var updateSearch = function(query) {
    window.state.search = query;

    // TODO: add to filter bar

    doFilter();
};

/**
 * Do the tag filter and search query, redraw the table, and do any post-filter
 * actions
 */
var doFilter = function() {
    table.search(window.state.search).draw();

    // TODO: show/hide filter bar

    // always save state so user can navigate back to same state
    if (window.location.hash === "") {
        window.history.pushState(window.state, "", "#filter");
    } else {
        window.history.replaceState(window.state, "");
    }
};

/**
 * Load previously saved state
 */
var applyState = function() {
    // clear filters bar
    $(".filters-list").empty();

    var state = window.history.state;
    $.each(state.filters, function(i, val) {
        addFilter(val);
    });

    var query = state.search;
    $(".search-bar input").val(query);
    doFilter(query);
};

/**
 * Going from / to #filter or vice versa
 */
window.onpopstate = function() {
    // #filter to /
    if (window.history.state === null) {
        window.location = "";
    } else {
        applyState();
    }
};
