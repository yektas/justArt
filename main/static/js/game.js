$(document).ready(function () {

    $("#answers").on("click", "button", function (event) {
        event.preventDefault();
        var form = $(this).closest("form");
        var questionId = form.serializeArray();
        var choice = $(this).text();
        questionId.forEach(function (item) {
            console.log(item['name=[csrfmiddlewaretoken]']);
        })
    });

    function sendChoice(questionId, choice) {

        var url = window.location.protocol + "//" + window.location.host + "/main/check-answer";
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
            isOver = true;
            clearInterval(mainLoop)
        }
        else {
            timer.innerHTML = new_time;
        }
    }


});