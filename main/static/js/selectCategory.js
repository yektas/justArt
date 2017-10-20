$(document).ready(function () {

    $(".select-category").on("click", function (event) {
        event.preventDefault();
        var form = $(this).closest("form");
        var csrf = form.find("input[name='csrfmiddlewaretoken']").val();
        var category = form.find("input[name='category']").val();
        var url = window.location.protocol + "//" + window.location.host + "/set-category";
        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken: csrf,
                category: category
            },
            success: function (data) {
                var url = window.location.protocol + "//" + window.location.host + "/game";
                setTimeout(function () {
                    window.location = url;
                }, 1000);
            }
        });
    });

});