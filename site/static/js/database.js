var HEADER_HEIGHT, FILTER_BAR_HEIGHT, table;
window.state = {
    options: {
        title: true,
        artist: true,
        tags: true,
        lyrics: true,
    },
    filters: [],
    search: "",
};

$(document).ready(function() {
    // set up constants
    HEADER_HEIGHT = $("header").outerHeight();
    FILTER_BAR_HEIGHT = $(".status-bar").outerHeight();

    // add in lyrics column dynamically to avoid showing it in lack of Javascript
    $("<th>")
        .text("Lyrics")
        .appendTo(".songs-table thead tr");

    $(".songs-table tbody tr").each(function() {
        var lyrics = $(this).data("lyrics");
        $("<td>")
            .text(lyrics)
            .appendTo(this);
    });

    var options = {
        dom: "t",
        paging: false,
        order: [[0, 'asc']],
        columnDefs: [
            {
                targets: 2,
                orderable: false,
            },
            {
                targets: 4,
                visible: false,
            },
        ],
        language: {
            zeroRecords: "No songs found",
        },
    };

    table = $(".songs-table").DataTable(options);
    // allow dynamic resizing
    $(".songs-table").css("width", "");

    // set up scroll
    $(window)
        .scroll(function() {
            // header is showing
            if ($(this).scrollTop() < HEADER_HEIGHT) {
                $(".status-bar").removeClass("sticky");
            } else {
                $(".status-bar").addClass("sticky");
            }
        })
        // trigger to initialize
        .scroll();

    // add filter interactions
    $(".songs-table")
        .find(".themes a, .speed a")
        .click(function() {
            var tag = $(this).text();
            if (isFilter(tag)) {
                removeFilter(tag);
            } else {
                addFilter(tag);
            }
            return false;
        });

    // set up search bar
    $(".search-bar input").keyup(function() {
        updateSearch($(this).val());
    });

    // set up search options
    $(".search-bar .search-options").click(function() {
        var options = $(".search-bar .options");
        if ($(this).hasClass("active")) {
            options
                .slideUp(400)
                .removeClass("active");
            $(this).removeClass("active");
        } else {
            options
                .slideDown(400)
                .addClass("active");
            $(this).addClass("active");
        }
        return false;
    });
    $(".search-bar .options input[type=checkbox]").click(function() {
        updateOptions(this);
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
 * Returns true if the given tag is already being filtered on
 */
var isFilter = function(tag) {
    return window.state.filters.indexOf(tag) !== -1;
};

/**
 * Adds filter to the state and the status bar and redraws table
 */
var addFilter = function(tag) {
    if (isFilter(tag)) {
        return;
    }

    // update filter list
    window.state.filters.push(tag);

    // update status bar
    var item = $("<li>");
    $("<a>")
        .text(tag)
        .attr("href", "#")
        .appendTo(item)
        .click(function() {
            removeFilter($(this).text());
            return false;
        });
    $(".filter-list").append(item);

    doFilter();
};

/**
 * Removes filter from state and the status bar and redraws table
 */
var removeFilter = function(tag) {
    // update filter list
    var index = window.state.filters.indexOf(tag);
    window.state.filters.splice(index, 1);

    // update status bar
    $(".filter-list a")
        .filter(function() {
            return $(this).text() === tag;
        })
        .parent().remove();

    doFilter();
};

/**
 * Updates search query in state and status bar and redraws table
 */
var updateSearch = function(query) {
    window.state.search = query;
    $(".search-query").text(query);

    doFilter();
};

/**
 * Update search options in state and redraws table
 */
var updateOptions = function(checkbox) {
    var id = $(checkbox).attr("id").replace("search-", "");
    window.state.options[id] = $(checkbox).prop("checked");

    doFilter();
};

/**
 * Return a list of jQuery selectors from the given options
 */
var getColumns = function(options) {
    return $.map(options, function(value, key) {
        if (!value) {
            return [];
        } else if (key === "tags") {
            return [".themes", ".speed"];
        } else {
            return "." + key;
        }
    });
};

/**
 * Do the tag filter and search query, redraw the table, and do any post-filter
 * actions
 */
var doFilter = function() {
    var filters = window.state.filters;
    var query = window.state.search;
    var options = window.state.options;

    var columns = getColumns(options);
    // TODO: fix
    console.log(columns);
    table
        .column(columns)
        .search(query)
        .draw();

    if (filters.length === 0 && query.length === 0) {
        $(".status-bar").hide();
        $(".content").css("margin-top", "");
    } else {
        $(".status-bar").show();
        $(".content").css("margin-top", FILTER_BAR_HEIGHT);

        // show/hide filters section
        if (filters.length === 0) {
            $(".filter-text").hide();
        } else {
            $(".filter-text").show();
        }

        // show/hide search section
        if (query.length === 0) {
            $(".search-text").hide();
        } else {
            $(".search-text").show();
        }
    }

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
    $(".filter-list").empty();

    var state = window.history.state;
    $.each(state.filters, function(i, val) {
        addFilter(val);
    });

    var query = state.search;
    $(".search-bar input").val(query);
    updateSearch(query);
    doFilter();
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
