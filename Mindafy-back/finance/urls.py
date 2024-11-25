from django.urls import path
from . import views

urlpatterns = [
    path('deposit/save/', views.save_deposit),
    path('deposit/', views.deposit),
    path('saving/save/', views.save_saving),
]