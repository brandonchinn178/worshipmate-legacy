// check if drag-n-drop is supported
var isAdvancedUpload = function() {
    var div = $("<div>")[0];
    var hasDragNDrop = ('draggable' in div) || ('ondragstart' in div && 'ondrop' in div);
    var hasDataTransfer = 'FormData' in window && 'FileReader' in window;
    return hasDragNDrop && hasDataTransfer;
}();

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
        .change()
        // can also initialize file text with data-filename attr
        .each(function() {
            var filename = $(this).parent().data("filename");
            if (filename.length !== 0) {
                updateFileText(this, filename);
            }
        });
    $(".song-form").submit(submitSongForm);

    // init theme popup
    $(".add-theme").click(function() {
        $("body").addClass("no-scroll");
        $(".theme-popup").show();
        $(".theme-popup [name=name]").focus();
        return false;
    });
    $(".theme-popup .submit").click(submitTheme);
    $(".theme-popup .cancel").click(function() {
        $("body").removeClass("no-scroll");
        $(".theme-popup").hide();
        return false;
    });

    // drag-n-drop feature (https://css-tricks.com/drag-and-drop-file-uploading/)
    if (isAdvancedUpload) {
        var droppedFiles = false;
        window.doc = null;
        window.pdf = null;
        $(".content")
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

var submitSongForm = function() {
    // if there are drag-n-dropped files, use AJAX to submit form
    var isDoc = window.doc !== null;
    var isPdf = window.pdf !== null;
    if (isAdvancedUpload && (isDoc || isPdf)) {
        var data = new FormData();
        // populate with text data
        $(this).find("input, textarea, .speed select").each(function() {
            var name = $(this).attr("name");
            if (name === undefined || name === "doc" || name === "pdf") {
                return;
            }
            data.append(name, $(this).val());
        });
        // individually add each theme
        var themes = $(this).find(".themes select").val() || [];
        $.each(themes, function(i, theme) {
            data.append("themes", theme);
        });
        // set file data
        if (isDoc) {
            data.append("doc", window.doc);
        } else {
            data.append("doc", $(".field.doc input").val());
        }
        if (isPdf) {
            data.append("pdf", window.pdf);
        } else {
            data.append("pdf", $(".field.pdf input").val());
        }
        data.append("action", "save-song");

        $.ajax({
            url: "",
            method: "POST",
            data: data,
            dataType: "json",
            cache: false,
            contentType: false,
            processData: false,
            success: function(data) {
                // TODO: redirect
            },
            error: function(xhr) {
                // TODO: extract errors from xhr.responseJSON
            },
        });

        return false;
    }
};

var submitTheme = function() {
    var popup = $(this).parents(".popup");
    var data = {
        action: "add-theme",
        name: getVal(popup, "name"),
    };
    postData(popup, {
        data: data,
        success: function(data) {
            // add theme to themes list
            $("<option>")
                .attr("value", data.id)
                .prop("selected", true)
                .text(data.name)
                .appendTo("#id_themes");
            $("#id_themes").trigger("chosen:updated");

            $("<li>")
                .text("Successfully added \"" + data.name + "\"")
                .appendTo(".theme-popup .feedback");
            $(".theme-popup [name=name]").val("");
        },
    });
    return false;
};
