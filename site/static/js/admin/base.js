/**
 * This file contains various utility functions for admin javascript files
 */

/**
 * Gets the value of the input/select/textarea with the given name, in the given container
 */
var getVal = function(container, name) {
    return $(container).find("[name=" + name + "]").val();
};

var sendAjax = function(options) {
    var defaults = {
        url: "",
        method: "POST",
        dataType: "json",
    };
    var settings = $.extend(defaults, options);

    // get/set CSRF
    var token = getVal($("body"), "csrfmiddlewaretoken");
    if (settings.data instanceof FormData) {
        settings.data.append("csrfmiddlewaretoken", token);
    } else {
        settings.data.csrfmiddlewaretoken = token;
    }
    $.ajax(settings);
};

/**
 * Runs an AJAX call with the given settings, which should contain the
 * POST data (without the CSRF token) and a success function.
 */
var postData = function(popup, settings) {
    // clear any messages
    var feedback = popup.find(".feedback").empty();
    if (feedback.length === 0) {
        var box = popup.find(".wrapper");
        feedback = $("<ul>")
            .addClass("feedback")
            .appendTo(box);
    }

    var defaults = {
        error: function(xhr) {
            var text = "An error occurred";
            if (xhr.responseJSON !== undefined) {
                text = xhr.responseJSON.message;
            }
            $("<li>")
                .addClass("error")
                .text(text)
                .appendTo(feedback);
            console.error(xhr);
        },
    };
    var ajaxSettings = $.extend(defaults, settings);
    sendAjax(ajaxSettings);
};
