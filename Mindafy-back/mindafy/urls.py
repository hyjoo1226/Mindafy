from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/v1/tests/', include('tests.urls')),
    path('api/v1/comments/', include('comments.urls')),
]
