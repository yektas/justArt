$(document).ready(function () {

    getQuestions();


    $("#answers").on("click", "button", function (event) {
        event.preventDefault();
        var pact_value = $(this).val();
        var choice = pact_value.split(",")[0];
        var questionId = $(".question-image").attr("id");
        sendChoice(questionId, choice);
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
                $(".question-image").prop("id", json.question.id);
                for (var i = 1; i < 5; i++) {
                    var choice = $("#choice" + i);
                    var artist_name = json.question.choices[i - 1][0];
                    var movement = json.question.choices[i - 1][1];
                    var artist_movement = json.question.choices[i - 1];
                    choice.val(artist_movement);
                    choice.text(artist_name + " (" + movement + ")");
                }

            }
        });
    }

    function sendChoice(questionId, choice) {

        var url = window.location.protocol + "//" + window.location.host + "/check-answer";
        var csrf = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken: csrf,
                questionId: questionId,
                choice: choice
            },
            success: function (data) {
                alert(data);
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
            clearInterval(mainLoop);
        }
        else {
            timer.innerHTML = new_time;
        }
    }


});