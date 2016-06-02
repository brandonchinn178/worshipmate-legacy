$(document).ready(function() {
    $(".song-form .delete").click(function() {
        $(".delete-popup").show();
        return false;
    });
    $(".delete-popup .cancel").click(function() {
        $(".delete-popup").hide();
        return false;
    });
});
