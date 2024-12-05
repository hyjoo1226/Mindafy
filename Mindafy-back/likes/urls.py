from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_like),
    path('comment/', views.comment_like),
]
