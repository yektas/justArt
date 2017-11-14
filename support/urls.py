from django.conf.urls import url

from support import views

app_name = 'support'

urlpatterns = [
    url(r'^support_foundation$', views.support_foundation, name='support_foundation'),
]
