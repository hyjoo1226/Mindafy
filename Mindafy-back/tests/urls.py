from django.urls import path
from . import views

urlpatterns = [
    path('', views.tests),
    path('<int:test_id>/', views.test_detail),
]
