from django.conf.urls import url

from main import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game$', views.game, name='game'),
    url(r'^set-category$', views.setCategory, name='set_category'),
    url(r'^set-questions$', views.setQuestions, name='set_questions'),
    url(r'^check-answer$', views.checkAnswer, name='check_answer'),
    url(r'end-screen$', views.endScreen, name='end_screen'),
]
