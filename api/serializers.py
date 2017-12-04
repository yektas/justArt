from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import Question, Artist, Category
from support.models import Foundation
from user.models import UserProfile, Result


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'category_name'
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name'
        ]


class QuestionSerializer(ModelSerializer):
    answer = serializers.StringRelatedField()
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'id',
            'questionImage',
            'answer',
            'point',
            'category',
        ]


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            'id',
            'artist_name'
        ]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer

    class Meta:
        model = UserProfile
        fields = [
            'user',
            'play_count',
            'support_count'
        ]


class FoundationSerializer(ModelSerializer):
    class Meta:
        model = Foundation
        fields = [
            'id',
            'foundation_name',
            'logo',
            'about',
            'support_count',
        ]


class ResultSerializer(ModelSerializer):
    user = UserSerializer
    category = CategorySerializer

    class Meta:
        model = Result
        fields = [
            'id',
            'user',
            'category',
            'point',
            'played_date'
        ]
