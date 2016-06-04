var table;

$(document).ready(function() {
    // set up action links
    var editLink = $("<a>")
        .addClass("edit")
        .attr("href", "#")
        .click(function() {
            $("body").addClass("no-scroll");

            var row = $(this).parents("tr");
            var id = row.attr("id");
            var name = row.find(".name").text();
            $(".edit-popup input[name=pk]").val(id);
            $(".edit-popup input[name=name]").val(name);
            $(".edit-popup").show();
            $(".edit-popup input[name=name]").focus();
            return false;
        });;
    var deleteLink = $("<a>")
        .addClass("delete")
        .attr("href", "#")
        .click(function() {
            $("body").addClass("no-scroll");

            var row = $(this).parents("tr");
            var id = row.attr("id");
            var name = row.find(".name").text();
            $(".delete-popup input[name=pk]").val(id);
            $(".delete-popup .theme-name").text(name);
            $(".delete-popup").show();
            return false;
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
        drawCallback: function() {
            this.$("td.actions").each(function() {
                if ($(this).children().length === 0) {
                    editLink.clone(true).appendTo(this);
                    deleteLink.clone(true).appendTo(this);
                }
            });
        },
    };

    table = $(".themes-table").DataTable(options);

    // set up popups
    $(".add-theme").click(function() {
        $("body").addClass("no-scroll");
        $(".add-popup").show();
        $(".add-popup [name=name]").focus();
        return false;
    });

    // set up popup buttons
    $(".add-popup .submit").click(addTheme);
    $(".edit-popup .submit").click(editTheme);
    $(".delete-popup .delete").click(deleteTheme);
    $(".popup .cancel").click(function() {
        $("body").removeClass("no-scroll");
        $(this).parents(".popup").hide();
        return false;
    });
});

var addTheme = function() {
    var popup = $(this).parents(".popup");

    var data = {
        action: "add",
        name: getVal(popup, "name"),
    };
    postData(popup, {
        data: data,
        success: function(data) {
            $("<li>")
                .text("Successfully added \"" + data.name + "\"")
                .appendTo(".add-popup .feedback");
            $(".add-popup [name=name]").val("");
            table
                .row.add([data.name, 0])
                .draw();

            // add id to row
            $(".themes-table tbody tr")
                .filter(function() {
                    return $(this).attr("id") === undefined;
                })
                .attr("id", data.id);
        },
    });
    return false;
};

var editTheme = function() {
    var popup = $(this).parents(".popup");

    var data = {
        action: "edit",
        pk: getVal(popup, "pk"),
        name: getVal(popup, "name"),
    };
    postData(popup, {
        data: data,
        success: function(data) {
            table
                .row("#" + data.id)
                .data([data.name, data.songs])
                .draw();
            $(".edit-popup .cancel").click();
        },
    });
    return false;
};

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
