from django.conf.urls import url

from api.views import QuestionListAPIView, QuestionDetailAPIView, ArtistListAPIView, FoundationListAPIView, \
    UserListAPIView, UserCreateAPIView, UserDetailAPIView, ResultListAPIView, ResultDetailAPIView

app_name = 'api'

urlpatterns = [

    url(r'^questions/$', QuestionListAPIView.as_view(), name='list_questions'),
    url(r'^question/(?P<id>\d+)/$', QuestionDetailAPIView.as_view(), name='question_detail'),

    url(r'^artists/$', ArtistListAPIView.as_view(), name='list_artists'),

    url(r'^foundations/$', FoundationListAPIView.as_view(), name='list_foundations'),

    url(r'^users/$', UserListAPIView.as_view(), name='list_users'),
    url(r'^user/(?P<id>\d+)/$', UserDetailAPIView.as_view(), name='user_detail'),
    url(r'^create-user/$', UserCreateAPIView.as_view(), name='create_user'),

    url(r'^results/$', ResultListAPIView.as_view(), name='list_results'),
    url(r'^result/(?P<id>\d+)/$', ResultDetailAPIView.as_view(), name='result_detail'),
]
