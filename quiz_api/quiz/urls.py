from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizCategoryViewSet, QuestionViewSet, AnswerViewSet, ScoreViewSet

router = DefaultRouter()
router.register(r'categories', QuizCategoryViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Inclui todas as rotas automaticamente
]
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Gera token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Renova token
]
