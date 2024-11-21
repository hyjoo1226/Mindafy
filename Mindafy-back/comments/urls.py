from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments),
    # path('<int:test_id>/', views.test_detail),
]
