from django.urls import path
from . import views

urlpatterns = [
    path('', views.comments),
    path('<int:comment_id>/', views.comment_detail),
    path('create/', views.create_comment),
]
