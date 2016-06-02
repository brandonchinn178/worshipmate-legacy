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

    // TODO: add theme popup
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
