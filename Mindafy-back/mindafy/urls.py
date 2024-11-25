from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/v1/tests/', include('tests.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('api/v1/surveys/', include('surveys.urls')),
    path('api/v1/finance/', include('finance.urls')),
]
