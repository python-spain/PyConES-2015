/**!
 * Little Javascript for PyConES web :)
 */
(function(){
    $(document).ready(function(){
        $(".slot-inner").on("click", function(event) {
            var description = $("#slot-description-" + $(this).data("slot"));
            //if (description.hasClass("hidden")) {
            //    description.removeClass("hidden");
            //}
            //else {
            //    description.addClass("hidden");
            //}
            description.fadeToggle();
        });
    });
})();