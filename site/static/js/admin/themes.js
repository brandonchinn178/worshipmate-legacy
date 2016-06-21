var table;

$(document).ready(function() {
    var options = {
        dom: "t",
        paging: false,
        order: [[0, 'asc']],
        columnDefs: [
            {
                targets: 2,
                orderable: false,
            },
        ],
        columns: [
            {
                className: "name",
            },
            {
                className: "songs",
            },
            {
                className: "actions",
            },
        ],
    };

    table = $(".themes-table").DataTable(options);
    $("td.actions a.delete").click(function() {
        $("body").addClass("no-scroll");

        var row = $(this).parents("tr");
        var id = row.attr("id");
        var name = row.find(".name").text();
        $(".delete-popup input[name=pk]").val(id);
        $(".delete-popup .theme-name").text(name);
        $(".delete-popup").show();
        return false;
    });

    // set up popup buttons
    $(".delete-popup .delete").click(deleteTheme);
    $(".delete-popup .cancel").click(function() {
        $("body").removeClass("no-scroll");
        $(this).parents(".popup").hide();
        return false;
    });
});

var deleteTheme = function() {
    var popup = $(this).parents(".popup");

    var data = {
        action: "delete",
        pk: getVal(popup, "pk"),
    };
    postData(popup, {
        data: data,
        success: function(data) {
            table
                .row("#" + data.id)
                .remove()
                .draw();
            $(".delete-popup .cancel").click();
        },
    });
    return false;
};
