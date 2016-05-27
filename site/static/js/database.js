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
        doSearch($(this).val());
    });

    // update state
    if (window.history.state !== null) {
        applyState(window.history.state);
    }
});

var addFilter = function(tag) {
    // if tag already being filtered, remove instead
    if (window.state.filters.indexOf(tag) !== -1) {
        return removeFilter(tag);
    }

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

    window.state.filters.push(tag);
    $(".filters-list").append(item);

    doFilter();

    if (window.state.filters.length === 1) {
        $(".filter-bar").show();
        $(".content").css("margin-top", FILTER_BAR_HEIGHT);
    }

    updateState();
};

var removeFilter = function(tag) {
    var index = window.state.filters.indexOf(tag);
    window.state.filters.splice(index, 1);
    $(".filters-list a").each(function() {
        if ($(this).text() === tag) {
            $(this).parent().remove();
        }
    });

    doFilter();

    if (window.state.filters.length === 0) {
        $(".filter-bar").hide();
        $(".content").css("margin-top", "");
    }

    updateState();
};

/**
 * Do our own filter algorithm, instead of the DataTables search function
 *
 * TODO: fix re-coloring issue
 */
var doFilter = function() {
    var filters = window.state.filters;
    $(".songs-table tbody tr")
        .hide()
        .each(function() {
            var tags = $(this)
                .find(".themes")
                .text()
                .split(", ");
            var speed = $(this).find(".speed").text();
            // Fast/Slow also acts as both Fast and Slow
            if (speed === "Fast/Slow") {
                tags.push("Fast");
                tags.push("Slow");
            }
            tags.push(speed);

            for (var i = 0; i < filters.length; i++) {
                if (tags.indexOf(filters[i]) === -1) {
                    return;
                }
            }
            $(this).show();
        });
};

// TODO: add to filter list
var doSearch = function(query) {
    table.search(query).draw();

    // no matches
    if ($(".songs-table tbody tr:visible").length === 0) {
        var emptyText = "No songs found for: " + query;
        var empty = $(".songs-table .dataTables_empty");
        // all rows with search hidden by filter
        if (empty.length === 0) {
            var cell = $("<td>")
                .text(emptyText)
                .attr("colspan", "100");
            $("<tr>")
                .addClass("empty-row")
                .append(cell)
                .appendTo(".songs-table tbody");
        } else {
            empty.text(emptyText);
        }
    } else {
        $(".songs-table tbody .empty-row").remove();
    }

    window.state.search = query;
    updateState();
};

/**
 * When filtering, always save state so user can navigate back to same state
 */
var updateState = function() {
    if (window.location.hash === "") {
        window.history.pushState(window.state, "", "#filter");
    } else {
        window.history.replaceState(window.state, "");
    }
};

/**
 * Load previously saved state
 */
var applyState = function(state) {
    $.each(state.filters, function(i, val) {
        addFilter(val);
    });

    var query = state.search;
    $(".search-bar input").val(query);
    doSearch(query);
};

/**
 * Going from / to #filter or vice versa
 */
window.onpopstate = function() {
    var state = window.history.state;
    // #filter to /
    if (state === null) {
        window.location = "";
    } else {
        applyState(state);
    }
};
