$(document).on('click', '.supportBtn', function (event) {
    event.preventDefault();
    var form = $(this).closest("form");
    var foundation_id = form.find(':input[name="foundation"]').val();
    var url = window.location.protocol + "//" + window.location.host + "/support/support_foundation";
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: csrftoken,
            foundation_id: foundation_id
        },
        success: function (data) {
            $('[data-id="' + foundation_id + '"]').text(data);
        },
    });
});
