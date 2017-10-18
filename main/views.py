from django.shortcuts import render

from main.models import Question, Choice


def index(request):

    return render(request, "index.html")


def game(request):
    if request.method == 'POST':
        category = request.POST.get("category", " ")
        question = Question.objects.get(category__category_name=category)

        # Sorunun cevabını listemize ekliyoruz en başta
        choices = [str(question.answer)]
        # Şıkları dolduruyoruz
        for i in range(3):
            choice = Choice.randoms.random()
            # Aynı ise başka bir seçenek alıyoruz
            while str(choice) in choices:
                choice = Choice.randoms.random()
            choices.append(str(choice))
        payload = {
            'image': str(question.questionImage),
            'choices': choices,
            'point': question.point
        }
    return render(request, "game.html", {"question": payload})
