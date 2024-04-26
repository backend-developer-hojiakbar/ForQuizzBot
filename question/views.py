from rest_framework import generics
from .models import Answer
from .serializers import AnswerSerializer


class AnswerListView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

