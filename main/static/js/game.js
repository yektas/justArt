$(document).ready(function () {

    var canvas = $("#mainContainer");
    var question = document.createElement("div");
    var questionImage = document.createElement("img");
    questionImage.setAttribute("src", "http://via.placeholder.com/1000x500");
    questionImage.setAttribute("class", "img-responsive");
    question.appendChild(questionImage);
    canvas.append(question)

});