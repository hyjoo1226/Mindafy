from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tests),
    path('<int:test_id>/', views.test_detail),
    path('<int:test_id>/comments/', include('comments.urls')),
    path('<int:test_id>/likes/', include('likes.urls')),
    path('<int:test_id>/surveys/', include('surveys.urls')),
    path('<int:test_id>/start/', views.create_test_result),
    path('results/<int:test_result_id>/surveys/', include('surveys.urls')),
    path('results/', views.test_results),
    path('results/<int:test_result_id>/', views.test_result_detail),
]