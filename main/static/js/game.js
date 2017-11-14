var clickSound = new Audio(clickSrc);
var correctSound = new Audio(correctSrc);
var wrongSound = new Audio(wrongSrc);
var background = document.getElementById("background-audio");
background.loop = true;
volume = 0.1;
background.volume = volume;

var progress = 0;
var questions = [];

var mainLoop;
setQuestions();
renderQuestion(questions);
window.onload = function () {
    $("#loader-wrapper").fadeOut(700, function () {
        $(this).remove();
    });
    mainLoop = setInterval(Timer, 1000);
    background.play();
};



// Gelen soruyu render lar.
function renderQuestion(questions) {
    progress += 1;
    if (questions.length !== 0) {
        var question_data = questions.pop();
        var questionSrc = '/media/' + question_data.image;
        $("#question").prop("src", questionSrc);
        $(".question-image").prop("id", question_data.id);
        for (var i = 1; i < 5; i++) {
            var choice = $("#choice" + i);
            var artist_name = question_data.choices[i - 1][0];
            var movement = question_data.choices[i - 1][1];
            var artist_movement = question_data.choices[i - 1];
            choice.val(artist_movement);
            choice.text(artist_name + " (" + movement + ")");
        }
        $('#answers').click(false);
        $("#timer").text("20");
        $("#currentQuestion").text(progress);
    }
    // Sorular bitti burada bitiş ekranına geçicez.
    else {
        $("#fakeLoader").fakeLoader({
            timeToHide: 2000, //Time in milliseconds for fakeLoader disappear
            zIndex: "999",//Default zIndex
            spinner: "spinner1",//Options: 'spinner1', 'spinner2', 'spinner3', 'spinner4', 'spinner5', 'spinner6', 'spinner7'
            bgColor: "#2ecc71", //Hex, RGB or RGBA color
        });

        // Arkaplan müziğinin sesini azar azar kısıyoruz.
        function fadeVolume(volume, callback) {
            var factor = 0.01,
                speed = 150;
            if (volume > factor) {
                setTimeout(function () {
                    fadeVolume((background.volume -= factor), callback);
                }, speed);
            } else {
                (typeof(callback) !== 'function') || callback();
            }
        }

        fadeVolume(background.volume);
        clearInterval(mainLoop);

        $.get("/end-screen", function (data) {
            $("#mainContainer").html(data);
        });
    }
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
                    html: "<h2 style='color:#fff'> Doğru <h2>",
                    type: 'success',
                    timer: 1200,
                    background: 'transparent',
                    showConfirmButton: false,
                }).catch(swal.noop);
            }
            else if (json.answer === false) {
                wrongSound.play();
                button.classList.add("btn-danger");
                swal({
                    html: "<h2 style='color:#fff'> Yanlış <h2>",
                    type: 'error',
                    timer: 1200,
                    background: 'transparent',
                    showConfirmButton: false
                }).catch(swal.noop);
            }
            //Puanı güncelle
            $("#point").text(json.point);

            var delayMillis = 1500; //1.5 seconds
            setTimeout(function () {
                renderQuestion(questions);
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

function Timer() {
    var timer = document.getElementById("timer");
    var currentTimer = timer.innerHTML;
    var new_time = parseInt(currentTimer) - 1;
    if (new_time < 0) {
        clearInterval(mainLoop);
        swal({
            html: "<h2 style='color:#fff'> Süre Doldu <h2>",
            type: 'error',
            background: 'transparent',
            timer: 1200,
            showConfirmButton: false
        }).catch(swal.noop);
        setTimeout(function () {
            renderQuestion(questions);
            mainLoop = setInterval(Timer, 1000);
        }, 1000);
    }
    else {
        timer.innerHTML = new_time;
    }
}

// Soruları backend den çekip questions array ine atıyoruz.
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
            questions = JSON.parse(data);
            var totalQuestion = document.getElementById("totalQuestion");
            totalQuestion.innerHTML = questions.length;
        },

    });
}

function controlBackgroundMusic() {
    var icon = $("#controlMusic > i");
    var button = $("#controlMusic");
    if (background.paused) {
        button.html("<i class='fa fa-fw fa-volume-up'></i> Müziği Kapat");
        background.play();
    }
    else {
        button.html("<i class='fa fa-fw fa-volume-off'></i> Müziği Aç");
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
