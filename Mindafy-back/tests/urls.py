from django.urls import path
from . import views

urlpatterns = [
    path('tests/', views.tests),
    path('tests/<int:test_pk>/', views.test_detail),
]
