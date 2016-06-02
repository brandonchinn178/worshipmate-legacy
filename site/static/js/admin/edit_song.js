$(document).ready(function() {
    $(".song-form .delete").click(function() {
        $("body").addClass("no-scroll");
        $(".delete-popup").show();
        return false;
    });
    $(".delete-popup .cancel").click(function() {
        $("body").removeClass("no-scroll");
        $(".delete-popup").hide();
        return false;
    });
});
