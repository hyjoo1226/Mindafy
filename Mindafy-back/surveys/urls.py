from django.urls import path
from . import views

urlpatterns = [
    path('', views.surveys),
    # path('questions/', views.survey_questions),
    # path('answers/', views.survey_answers),
]
