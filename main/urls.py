from django.conf.urls import url

from main import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game$', views.game, name='game'),
    url(r'^check-answer$', views.checkAnswer, name='check_answer')
]
