$(document).on('click', '.supportBtn', function (event) {
    event.preventDefault();
    var support_button = $(this);
    var form = support_button.closest("form");
    var card = form.find(".card");
    var loader = card.find(".loader");
    loader.prop("src", loaderSvg);
    var content = form.find(".content");
    content.hide();
    loader.show();
    var foundation_id = form.find(':input[name="foundation"]').val();
    var url = window.location.protocol + "//" + window.location.host + "/support/support_foundation";
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var card = form.find(".card");
    var counter = $('[data-id="' + foundation_id + '"]');
    var up_arrow = counter.children();

    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: csrftoken,
            foundation_id: foundation_id
        },
        success: function (data) {
            loader.hide();
            content.fadeIn(700);
            counter.contents().filter(function () {
                return this.nodeType == 3;
            }).first().replaceWith(data);
            up_arrow.fadeIn("1000");
            support_button.replaceWith("<p>Harika, teşekkürler!</p>")
            var other_buttons = $(".supportBtn").not(support_button);
            other_buttons.css("visibility", "hidden");
        },
    });
});
