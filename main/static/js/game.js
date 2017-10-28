
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
            console.log(data);
            if (data === 'None') {
                $("#fakeLoader").fakeLoader({
                    timeToHide: 1200, //Time in milliseconds for fakeLoader disappear
                    zIndex: "999",//Default zIndex
                    spinner: "spinner1",//Options: 'spinner1', 'spinner2', 'spinner3', 'spinner4', 'spinner5', 'spinner6', 'spinner7'
                    bgColor: "#2ecc71", //Hex, RGB or RGBA color
                });

                // Burada oyun biticek ve sonuç ekranına yönlendiricez.

            }
            else {
                var clean_data = JSON.parse(data);
                renderQuestion(clean_data);
                //Kaçıncı soruda
                var progress = clean_data.progress;
                $("#currentQuestion").text(progress);
            }
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
    $("#timer").text("20");
}

// Cevap şıkkı seçildiği zaman;
function checkMyAnswer(button) {
    button.classList.remove("hvr-fade");
    clickSound.play();
    var pact_value = button.value;
    var choice = pact_value.split(",")[0];
    var questionId = $(".question-image").attr("id");
    sendChoice(questionId, choice, button);
}

// Seçilen cevabı backend e gönderip kontrol ediyoruz
function sendChoice(questionId, choice, button) {
    for (var i = 1; i < 5; i++) {
        document.getElementById("choice" + i).disabled = true;
    }
    var url = window.location.protocol + "//" + window.location.host + "/check-answer";
    var csrf = jQuery("[name=csrfmiddlewaretoken]").val();
    var time = $("#timer").text();
    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: csrf,
            questionId: questionId,
            choice: choice,
            time: time
        },
        success: function (data) {
            var json = JSON.parse(data);
            if (json.answer === true) {
                correctSound.play();
                button.classList.add("btn-success");
                swal({
                    title: 'Doğru',
                    type: 'success',
                    timer: 1500,
                    showConfirmButton: false
                })
            }
            else {
                wrongSound.play();
                button.classList.add("btn-danger");
                swal({
                    title: 'Yanlış',
                    type: 'error',
                    timer: 1500,
                    showConfirmButton: false
                })
            }
            //Puanı güncelle
            $("#point").text(json.point);

            var delayMillis = 1000; //1 second
            setTimeout(function () {
                getQuestion();
                if (button.classList.contains("btn-success")) {
                    button.classList.remove("btn-success");
        }
                else if (button.classList.contains("btn-danger")) {
                    button.classList.remove("btn-danger");
                }
                button.classList.add("btn-primary");
                button.classList.add("hvr-fade");
                for (var i = 1; i < 5; i++) {
                    document.getElementById("choice" + i).disabled = false;
                }

            }, delayMillis);
        },
    });
}

// Süreyi her saniye ekranda gösteriyoruz.
var mainLoop = setInterval(Timer, 1000);

function Timer() {
    var timer = document.getElementById("timer");
    var currentTimer = timer.innerHTML;
    var new_time = parseInt(currentTimer) - 1;
    if (new_time < 0) {
        clearInterval(mainLoop);
        swal({
            title: 'Süre Doldu',
            type: 'error',
            timer: 1000,
            showConfirmButton: false
        });
        setTimeout(function () {
            getQuestion();
            mainLoop = setInterval(Timer, 1000);
        }, 1000);



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
        async: false,
        data: {
            csrfmiddlewaretoken: csrftoken
        },
        success: function (data) {
            console.log("Yüklenen soru sayısı ", data)
            var totalQuestion = document.getElementById("totalQuestion");
            totalQuestion.innerHTML = data;
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
