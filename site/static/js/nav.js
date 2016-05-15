$(document).ready(function() {
    var nav = ["home", "database", "about", "contact"];
    nav.forEach(function(name) {
        var div = $(".nav-" + name);
        div.children("a").hover(function() {
            $(this).prev(".icon").addClass("active");
        }, function() {
            $(this).prev(".icon").removeClass("active");
        });
    });
    $("#searchbox").hide();
    $("#search").click(function(){
        if (!$("#searchbox").is(":visible")) {
            $("#searchbox").css('width', '0');
            $("#searchbox").show();
            $("#searchbox").animate({ width: "300px" });
            $("#searchbox").focus();
        } else {
            $("#searchbox").animate({ width: "0"});
            $("#searchbox").hide(1);
        }
    });
});