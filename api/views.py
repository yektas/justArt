from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from api.serializers import QuestionSerializer, ArtistSerializer, FoundationSerializer, UserSerializer, \
    ResultSerializer, UserProfileSerializer
from main.models import Question, Artist
from support.models import Foundation
from user.models import UserProfile, Result


class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailAPIView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'


class ArtistListAPIView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class FoundationListAPIView(ListAPIView):
    queryset = Foundation.objects.all()
    serializer_class = FoundationSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'id'


class ResultListAPIView(ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultDetailAPIView(RetrieveAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    lookup_field = 'id'
