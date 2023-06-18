from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionCreateSerializer, QuestionSerializer


# Create your views here.
class QuestionAPIView(APIView):
    def get(self, request):
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuestionCreateAPIView(APIView):
    def post(self, request):
        serializer = QuestionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = {'message': 'Question created successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(data = {'message': 'Failed to create question. Bad input.', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
