import json

from django.http import HttpResponse
from django.shortcuts import render

from main.models import Question


def index(request):
    return render(request, "index.html")


def game(request):
    return render(request, "game.html")


def get_questions(request):
    question = Question.objects.get(pk=2)
    questions = question.get_content
    data = {
        'question': questions[0],
        'answers': questions[1],
        'point': questions[2],
        'category': questions[3]
    }
    return HttpResponse(json.dumps(data))
