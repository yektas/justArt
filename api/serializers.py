from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import Question
from user.models import UserProfile


class QuestionSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Question
        fields = ('id', 'questionImage', 'point', 'answer', 'category')