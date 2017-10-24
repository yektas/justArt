var clickSound = new Audio(clickSrc);
var correctSound = new Audio(correctSrc);
var wrongSound = new Audio(wrongSrc);
var background = document.getElementById("background-audio");
background.loop = true;
background.volume = 0.1;
background.play();
setQuestions();
getQuestion();


// Soruyu backend den çekiyoruz.
function getQuestion() {
    var url = window.location.protocol + "//" + window.location.host + "/get-question";
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: "POST",
        url: url,
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
    $('#answers').click(false);

}

// Cevap şıkkı seçildiği zaman;
function checkMyAnswer(button) {
    var timer = $("#timer");
    console.log(timer.text());
    clickSound.play();
    var pact_value = button.value;
    console.log(pact_value);
    var choice = pact_value.split(",")[0];
    var questionId = $(".question-image").attr("id");
    sendChoice(questionId, choice, button);
}

// Sonraki soru için hazırlıklar;
function nextQuestion() {
}

// Seçilen cevabı backend e gönderip kontrol ediyoruz
function sendChoice(questionId, choice, button) {
    $("#answers").addClass("disabled");
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
            var json = JSON.parse(data);
            if (json.answer === true) {
                correctSound.play();
                button.classList.add("btn-success");
            }
            else {
                wrongSound.play();
                button.classList.add("btn-danger");
            }
        },
        complete: function () {
            $("#answers").removeClass("disabled");
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


function controlBackgroundMusic() {
    var button = $("#controlMusic");
    if (background.paused) {
        button.text("Müziği Kapat");
        background.play();
    }
    else {
        button.text("Müziği Aç");
        background.pause();
    }
}

// Telefonlar için tıkladığında müziği başlatma
var touchCount = 0;
document.addEventListener('touchstart', function () {
    if (touchCount = 0) {
        document.getElementsByTagName('audio')[0].play();
        touchCount += 1;
    }
});