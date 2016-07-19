// check if drag-n-drop is supported
var isAdvancedUpload = function() {
    var div = $("<div>")[0];
    var hasDragNDrop = 'ondragstart' in div && 'ondrop' in div;
    var hasDataTransfer = 'FormData' in window && 'FileReader' in window;
    return hasDragNDrop && hasDataTransfer;
}();

$(document).ready(function() {
    $(".artist select").selectize({
        create: true,
    });
    $(".themes select").selectize({
        create: addTheme,
    });
    $(".speed select").chosen({
        placeholder_text_single: " ",
        disable_search: true,
    });
    $("input[type=file]")
        .change(onFileChange)
        // initialize file text
        .change()
        // can also initialize file text with data-filename attr
        .each(function() {
            var filename = $(this).parent().data("filename");
            if (filename.length !== 0) {
                updateFileText(this, filename);
            }
        });
    $(".song-form").submit(submitSongForm);

    // drag-n-drop feature (https://css-tricks.com/drag-and-drop-file-uploading/)
    window.doc = null;
    window.pdf = null;
    if (isAdvancedUpload) {
        $("body")
            .on("drag dragstart dragend dragover dragenter dragleave drop", function(e) {
                return false;
            })
            .on("dragenter dragstart", function() {
                $("body").addClass("no-scroll");
                $(".file-upload").show();
            })
        $(".file-upload")
            .on("dragleave dragend drop", function() {
                $("body").removeClass("no-scroll");
                $(".file-upload").hide();
            })
            .on("drop", function(e) {
                var droppedFiles = e.originalEvent.dataTransfer.files;
                $.each(droppedFiles, function(i, file) {
                    switch (file.type) {
                        case "application/msword":
                            window.doc = file;
                            updateFileText($(".field.doc input"), file.name);
                            break;
                        case "application/pdf":
                            window.pdf = file;
                            updateFileText($(".field.pdf input"), file.name);
                            break;
                        default:
                            // do nothing
                    }
                });
            });;
    }
});

var onFileChange = function() {
    if (this.files.length === 0) {
        updateFileText(this, "");
    } else {
        var file = this.files[0];
        // reset drag-n-drop file
        switch (file.type) {
            case "application/msword":
                window.doc = null; break;
            case "application/pdf":
                window.pdf = null; break;
            default: // do nothing
        }
        var filename = file.name;
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

/**
 * Submit form via AJAX in case of drag-n-drop files, plus keeps selected files in place
 */
var submitSongForm = function() {
    $("ul.feedback").remove();
    var data = new FormData();
    data.append("action", "save-song");
    data.append("title", getVal(this, "title"));
    data.append("artist", getVal(this, "artist"));
    data.append("lyrics", getVal(this, "lyrics"));
    data.append("speed", getVal(this, "speed"));

    var themes = $(this).find(".themes select").val() || [];
    $.each(themes, function(i, theme) {
        data.append("themes", theme);
    });

    if (window.doc === null) {
        data.append("doc", $(".field.doc input")[0].files[0]);
    } else {
        data.append("doc", window.doc);
    }
    if (window.pdf === null) {
        data.append("pdf", $(".field.pdf input")[0].files[0]);
    } else {
        data.append("pdf", window.pdf);
    }

    $("<p>")
        .addClass("message")
        .text("Saving...")
        .prependTo(".song-form .buttons");

    sendAjax({
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        success: function(data) {
            window.location = data.redirect;
        },
        error: function(xhr) {
            $(".song-form .buttons .message").remove();
            var errors = [xhr.responseText];
            if (xhr.responseJSON !== undefined) {
                var errors = xhr.responseJSON.errors;
                if (errors === undefined) {
                    errors = [xhr.responseJSON.message];
                }
            }
            var messages = $("<ul>").addClass("feedback");
            $.each(errors, function(i, error) {
                $("<li>")
                    .addClass("error")
                    .text(error)
                    .appendTo(messages);
            });
            messages.prependTo(".content");
            $("body").scrollTop(0);
        },
    });

    return false;
};

var addTheme = function(input, callback) {
    sendAjax({
        data: {
            action: "add-theme",
            name: input,
        },
        success: function(data) {
            callback({
                value: data.id,
                text: data.name,
            });
        },
    });
};
