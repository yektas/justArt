from django.conf.urls import url
from django.contrib.auth.views import LogoutView

from user import views

app_name = 'user'

urlpatterns = [
    url(r'^login/$', views.loginView, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.register, name='register'),
]
