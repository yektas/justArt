$(document).ready(function () {

    setQuestions();
    getQuestion();


    // Soruyu backend den çekiyoruz.
    function getQuestion() {
        var url = window.location.protocol + "//" + window.location.host + "/get-question";
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: url,
            async: false,
            data: {
                csrfmiddlewaretoken: csrftoken
            },
            success: function (data) {
                renderQuestion(JSON.parse(data));
            }
        });
    }

    // Gelen soruyu render lar.
    function renderQuestion(question_data) {
        var questionSrc = '/media/' + question_data.question.image;
        $("#question").prop("src", questionSrc);
        $(".question-image").prop("id", question_data.question.id);
        for (var i = 1; i < 5; i++) {
            var choice = $("#choice" + i);
            var artist_name = question_data.question.choices[i - 1][0];
            var movement = question_data.question.choices[i - 1][1];
            var artist_movement = question_data.question.choices[i - 1];
            choice.val(artist_movement);
            choice.text(artist_name + " (" + movement + ")");
        }
    }

    // Cevap şıkkı seçildiği zaman;
    $("#answers").on("click", "button", function (event) {
        event.preventDefault();
        var pact_value = $(this).val();
        var choice = pact_value.split(",")[0];
        var questionId = $(".question-image").attr("id");
        sendChoice(questionId, choice);
    });

    // Seçilen cevabı backend e gönderip kontrol ediyoruz
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

    // Süreyi her saniye ekranda gösteriyoruz.
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

    // Soruları session a atıyoruz.
    function setQuestions() {
        var url = window.location.protocol + "//" + window.location.host + "/set-questions";
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken: csrftoken
            },
            success: function (data) {
                console.log("Yüklenen soru sayısı ", data)
            }
        });
    }
});