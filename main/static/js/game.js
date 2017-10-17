$(document).ready(function () {
    var isOver = false;

    var url = window.location.protocol + "//" + window.location.host + "/questions";
    $.ajax({
        url: url,
        success: function (data) {
            console.log(JSON.parse(data))
        }
    });

    var mainLoop = setInterval(Timer, 1000);

    function Timer() {
        if (!isOver) {
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
    }
});