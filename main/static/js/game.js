$(document).ready(function () {

    getQuestions();



    $("#answers").on("click", "button", function (event) {
        event.preventDefault();
        var form = $(this).closest("form");
        var csrf = form.find("input[name='csrfmiddlewaretoken']").val();
        var category = form.find("input[name='choice']").val();
        sendChoice()
    });

    function getQuestions() {
        var url = window.location.protocol + "//" + window.location.host + "/get-questions";
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken: csrftoken
            },
            success: function (data) {
                var json = JSON.parse(data);
                var questionSrc = '/media/' + json.question.image;
                $("#question").prop("src", questionSrc);
                for (var i = 1; i < 5; i++) {
                    var choice = $("#choice" + i);
                    choice.text(json.question.choices[i - 1]);
                    choice.closest("input").prop("value", json.question.id)
                }

            }
        });
        var form = $(this).closest("form");
        var csrf = form.find("input[name='csrfmiddlewaretoken']").val();
        var category = form.find("input[name='category']").val();
    }

    function sendChoice(questionId, choice) {

        var url = window.location.protocol + "//" + window.location.host + "/check-answer";
        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                search_user: search_user
            },
            success: function (data) {
            }
        });
    }
    var mainLoop = setInterval(Timer, 1000);

    function Timer() {
        var timer = document.getElementById("timer");
        var currentTimer = timer.innerHTML;
        var new_time = parseInt(currentTimer) - 1;
        if (new_time < 0) {
            timer.innerHTML = 0;
            clearInterval(mainLoop)
        }
        else {
            timer.innerHTML = new_time;
        }
    }


});