from django.urls import path
from . import views

urlpatterns = [
    path('', views.surveys),
    path('<int:survey_id>/questions/', views.survey_questions),
    path('<int:survey_id>/options/', views.survey_options),
    path('<int:survey_id>/questions/<int:question_id>/options/', views.survey_option_detail),
    # path('answers/', views.survey_answers),
]
