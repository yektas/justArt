import json
from random import shuffle

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from justArt import settings
from main.models import Question, Artist
from support.models import Foundation

total_question_number = getattr(settings, 'TOTAL_QUESTION_NUMBER')


@login_required
def index(request):
    return render(request, "index.html")


@login_required
def game(request):
    request.session['correct'] = 0
    request.session['point'] = 0
    request.session['progress'] = 0
    return render(request, "game.html")


@login_required
def finished(request):
    if request.method == 'POST':
        total_point = request.session['point']
        correct_count = request.session['correct']
        question_count = request.session['question_count']

        foundations = Foundation.objects.all()
        total_support_count = Foundation.objects.get_support_count
        
        data = {
            'total_point': total_point,
            'correct_count': correct_count,
            'total_question': question_count,
            'foundations': foundations,
            'total_support_count': total_support_count
        }
        html = render_to_string('endScreen.html', data)
        return HttpResponse(html)

def setQuestions(request):
    if request.method == 'POST':
        request.session['question_count'] = 0
        category = request.session.get('category', 'mix')

        questions = Question.objects.filter(category__category_name=category)[:5]

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
        request.session['question_count'] = question_count

        return HttpResponse(question_count)


def getQuestion(request):
    if len(request.session['questions']) > 0:
        question = request.session['questions'].pop()
        request.session['progress'] += 1
        data = {
            'question': question,
            'progress': request.session['progress']
        }
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
            time = request.POST.get('time')
            request.session['correct'] += 1
            time_plus = int(time) * 10
            request.session['point'] += question.point + time_plus
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
