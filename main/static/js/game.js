$(document).ready(function () {
    var isOver = false;
    var countDown = setInterval(Timer, 1000);

    function Timer() {
        if (!isOver) {
            var timer = document.getElementById("timer");
            var currentTimer = timer.innerHTML;
            var new_time = parseInt(currentTimer) - 1;
            if (new_time < 0) {
                timer.innerHTML = 0;
                isOver = true;
                clearInterval(countDown)
            }
            else {
                timer.innerHTML = new_time;
            }
        }


    }

});