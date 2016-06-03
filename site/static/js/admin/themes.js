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
            null,
            {
                className: "actions",
                render: function() {
                    // will render in drawCallback
                    return "";
                },
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
    popup.find(".feedback").empty();

    var data = {
        csrfmiddlewaretoken: getVal(popup, "csrfmiddlewaretoken"),
        action: "add",
        name: getVal(popup, "name"),
    };
    $.ajax({
        type: "POST",
        url: "",
        data: data,
        dataType: "json",
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
        error: function() {
            $("<li>")
                .addClass("error")
                .text("There was an error saving")
                .appendTo(".add-popup .feedback");
        },
    });
    return false;
};

var editTheme = function() {
    var popup = $(this).parents(".popup");
    popup.find(".feedback").empty();

    var data = {
        csrfmiddlewaretoken: getVal(popup, "csrfmiddlewaretoken"),
        action: "edit",
        pk: getVal(popup, "pk"),
        name: getVal(popup, "name"),
    };
    $.ajax({
        type: "POST",
        url: "",
        data: data,
        dataType: "json",
        success: function(data) {
            table
                .row("#" + data.id)
                .data([data.name, data.songs])
                .draw();
            $(".edit-popup .cancel").click();
        },
        error: function() {
            $("<li>")
                .addClass("error")
                .text("There was an error saving")
                .appendTo(".edit-popup .feedback");
        },
    });
    return false;
};

var deleteTheme = function() {
    var popup = $(this).parents(".popup");
    popup.find(".feedback").empty();

    var data = {
        csrfmiddlewaretoken: getVal(popup, "csrfmiddlewaretoken"),
        action: "delete",
        pk: getVal(popup, "pk"),
    };
    $.ajax({
        type: "POST",
        url: "",
        data: data,
        dataType: "json",
        success: function(data) {
            table
                .row("#" + data.id)
                .remove()
                .draw();
            $(".delete-popup .cancel").click();
        },
        error: function() {
            $("<li>")
                .addClass("error")
                .text("There was an error deleting")
                .appendTo(".delete-popup .feedback");
        },
    });
    return false;
};

var getVal = function(popup, name) {
    return popup.find("input[name=" + name + "]").val();
};
