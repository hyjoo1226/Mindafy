from django.contrib import admin
from django.urls import path, include
from accounts.views import CustomRegisterView, CustomLoginView
# from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tests.urls')),
    path('accounts/login/', CustomLoginView.as_view()),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', CustomRegisterView.as_view()),
]
