import json
from random import shuffle

from django.http import HttpResponse
from django.shortcuts import render

from justArt import settings
from main.models import Question, Choice


def index(request):

    return render(request, "index.html")


def game(request):
    return render(request, "game.html")


def getQuestions(request):
    if request.method == 'POST':
        category = request.session['category']
        total_question_number = getattr(settings, 'TOTAL_QUESTION_NUMBER')

        questions = Question.objects.filter(category__category_name=category)[:1]

        question_list = {}
        for question in questions:
            # Sorunun cevabını listemize ekliyoruz en başta
            choices = [str(question.answer)]

            # Şıkları dolduruyoruz
            for i in range(3):
                choice = Choice.randoms.random()
                # Aynı ise başka bir seçenek alıyoruz
                while str(choice) in choices:
                    choice = Choice.randoms.random()
                choices.append(str(choice))

            # Şıkları karıştır
            shuffle(choices)

            question_dict = {
                "id": question.id,
                "image": str(question.questionImage),
                "choices": choices,
                "point": question.point
            }
            question_list['question'] = question_dict
        request.session['questions'] = question_list
        return HttpResponse(json.dumps(request.session['questions']))


def getNextQuestion(request):
    question_list = request.session['questions']


def checkAnswer(request):

    if request.method == 'POST':
        question_id = request.POST.get()
        choice = request.POST.get('choice')


def setCategory(request):
    if request.method == 'POST':
        category = request.POST.get("category")
        request.session['category'] = category
        return HttpResponse('')
