from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.comments),
    path('<int:comment_id>/', views.comment_detail),
    path('<int:comment_id>/likes/', include('likes.urls')),
]
