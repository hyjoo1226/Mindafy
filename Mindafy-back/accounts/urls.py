from django.urls import path
from dj_rest_auth import views as dj_rest_auth_views
from . import views

urlpatterns = [
    path('signup/', views.CustomRegisterView.as_view()),
    path('login/', views.CustomLoginView.as_view()),

    path('password/change/', dj_rest_auth_views.PasswordChangeView.as_view()),
]