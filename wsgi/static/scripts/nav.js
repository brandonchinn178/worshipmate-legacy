$(document).ready(function() {
    var nav = ["home", "database", "about", "contact"];
    for (i = 0; i < nav.length; i++) {
        var button = "#nav-" + nav[i];
        var icon = "#" + nav[i] + "-icon";
        $(icon).hide();

        var enterFunction = function(id) {
            return function() {
                $(id).drop();
            };
        }(icon);
        var exitFunction = function(id) {
            return function() {
                $(id).fadeOut();
            };
        }(icon);
        $(button).hover(enterFunction, exitFunction);
    }
});

(function($) {
    $.fn.drop = function() {
        this.css('top', '-100px');
        this.show();
        this.animate({ top: "0px" });
        return this;
    };
}( jQuery ));