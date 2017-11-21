from django.conf.urls import url
from django.contrib.auth.views import LogoutView, login

from user import views
from user.forms import LoginForm

app_name = 'user'

urlpatterns = [
    url(r'^login/$', login, name='login',
        kwargs={'template_name': 'registration/login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^previous-games/$', views.previous_games, name='previous_games')
]
