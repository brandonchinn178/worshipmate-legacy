var table;

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

    // make filter-bar fixed on scroll
    // filter on click, replace state including filter params
});
