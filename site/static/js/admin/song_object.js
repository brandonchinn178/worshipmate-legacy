$(document).ready(function() {
    $(".themes select").chosen({
        placeholder_text_multiple: "Start typing...",
    });
    $(".speed select").chosen({
        placeholder_text_single: " ",
        disable_search: true,
    });
    $("input[type=file]")
        .change(onFileChange)
        // initialize file text
        .change();

    // can also initialize file text with data-filename attr
    $("input[type=file]").each(function() {
        var filename = $(this).parent().data("filename");
        if (filename.length !== 0) {
            updateFileText(this, filename);
        }
    });

    // init theme popup
    $(".add-theme").click(function() {
        $("body").addClass("no-scroll");
        $(".theme-popup").show();
        return false;
    });
    $(".theme-popup .submit").click(submitTheme);
    $(".theme-popup .cancel").click(function() {
        $("body").removeClass("no-scroll");
        $(".theme-popup").hide();
        return false;
    });
});

var onFileChange = function() {
    if (this.files.length === 0) {
        updateFileText(this, "");
    } else {
        var filename = this.files[0].name;
        updateFileText(this, filename);
    }
};

/**
 * Add/update the file text next to the file input
 */
var updateFileText = function(input, text) {
    var parent = $(input).parent();
    var textbox = parent.find(".file-text");
    if (textbox.length === 0) {
        textbox = $("<p>")
            .addClass("file-text")
            .prependTo(parent);
    }

    if (text.length === 0) {
        text = "No file selected";
    }
    textbox.text(text);
};

var submitTheme = function() {
    var popup = $(this).parents(".theme-popup");
    var name = popup.find("[name=name]").val();
    if (name.length === 0) {
        return false;
    }
    var data = {
        csrfmiddlewaretoken: popup.find("input[name=csrfmiddlewaretoken]").val(),
        action: "add-theme",
        name: name,
    };
    $.ajax({
        type: "POST",
        url: "",
        data: data,
        dataType: "json",
        success: function(data) {
            // add theme to themes list
            $("<option>")
                .attr("value", data.id)
                .text(data.name)
                .appendTo("#id_themes");
            $("#id_themes").trigger("chosen:updated");

            $("<li>")
                .text("Successfully added \"" + name + "\"")
                .appendTo(".theme-popup .feedback");
            $(".theme-popup [name=name]").val("");
        },
        error: function(xhr) {
            console.log(xhr.responseText);
            $("<li>")
                .addClass("error")
                .text("There was an error saving")
                .appendTo(".theme-popup .feedback");
        },
    });
    return false;
};
