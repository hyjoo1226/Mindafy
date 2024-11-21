from django.urls import path
from . import views

urlpatterns = [
    path('tests/', views.tests),
    path('tests/<int:test_id>/', views.test_detail),
]
