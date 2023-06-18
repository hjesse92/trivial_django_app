from django.urls import path

from . import views


urlpatterns = [path("api/questions/", views.QuestionAPIView.as_view(), name="question-list"),
    path(
        "api/questions/create/", views.QuestionCreateAPIView.as_view(), name="question-create"
    ),
    ]
