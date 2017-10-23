import json
from random import shuffle

from django.http import HttpResponse
from django.shortcuts import render

from justArt import settings
from main.models import Question, Artist


def index(request):

    return render(request, "index.html")


def game(request):
    request.session['correct'] = 0
    request.session['point'] = 0
    request.session['progress'] = 0
    return render(request, "game.html")


def setQuestions(request):
    if request.method == 'POST':
        category = request.session.get('category', 'mix')
        total_question_number = getattr(settings, 'TOTAL_QUESTION_NUMBER')

        questions = Question.objects.filter(category__category_name=category)[:2]

        question_list = []
        for question in questions:
            # Sorunun cevabını listemize ekliyoruz en başta
            answer_movement = question.answer.movement_name.movement_name
            package = (str(question.answer), answer_movement)
            choices = [package]

            # Şıkları dolduruyoruz
            for i in range(3):
                artist = Artist.randoms.random()
                # Aynı ise başka bir seçenek alıyoruz
                while package in choices:
                    artist = Artist.randoms.random()
                    movement = artist.movement_name.movement_name
                    package = (str(artist), movement)
                choices.append(package)

            # Şıkları karıştır
            shuffle(choices)
            question_list.append({
                "id": question.id,
                "image": str(question.questionImage),
                "choices": choices,
                "point": question.point
            })
            # Soruları karıştır
            shuffle(question_list)

        request.session['questions'] = question_list
        question_count = len(request.session['questions'])
        return HttpResponse(question_count)


def getQuestion(request):
    if len(request.session['questions']) > 0:
        question = request.session['questions'].pop()
        request.session['progress'] += 1
        data = {'question': question,
                'progress': request.session['progress']}
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse(None)


def checkAnswer(request):

    if request.method == 'POST':
        question_id = request.POST.get('questionId')
        choice = request.POST.get('choice')
        question = Question.objects.get(id=question_id)
        if choice == question.answer.artist_name:
            # Cevap doğruysa doğru sayısı ve puanı arttıyoruz
            request.session['correct'] += 1
            request.session['point'] += question.point
            point = {
                'answer': True,
                'point': request.session['point']
            }
            return HttpResponse(json.dumps(point))
        else:
            point = {
                'answer': False,
                'point': request.session['point']
            }
            return HttpResponse(json.dumps(point))



def setCategory(request):
    if request.method == 'POST':
        category = request.POST.get("category")
        request.session['category'] = category
        return HttpResponse('')
