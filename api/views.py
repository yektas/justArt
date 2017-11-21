
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import QuestionSerializer
from main.models import Question


class GetQuestionsView(viewsets.ViewSet):
    """This class defines the create behavior of our rest api."""

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

