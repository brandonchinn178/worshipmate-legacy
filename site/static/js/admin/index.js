$(document).ready(function() {
    var options = {
        dom: "t",
        paging: false,
        order: [],
        columnDefs: [
            {
                targets: [2],
                orderable: false,
            },
        ],
        language: {
            zeroRecords: "No songs found",
        },
    };
    var table = $(".songs-table").DataTable(options);

    $(".search-bar").keyup(function() {
        var query = $(this).val();
        table.search(query).draw();
    });
});
