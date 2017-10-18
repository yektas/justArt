$(document).ready(function () {

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