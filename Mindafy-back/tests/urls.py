from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tests),
    path('<int:test_id>/', views.test_detail),
    path('<int:test_id>/comments/', include('comments.urls')),
    path('<int:test_id>/likes/', include('likes.urls')),
    path('<int:test_id>/surveys/', include('surveys.urls')),
]