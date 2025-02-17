from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import QuizCategory, Question, Answer, Score
from .serializers import QuizCategorySerializer, QuestionSerializer, AnswerSerializer, ScoreSerializer

class QuizCategoryViewSet(viewsets.ModelViewSet):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer
    permission_classes = [AllowAny]  # Protege os endpoints

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [AllowAny]
