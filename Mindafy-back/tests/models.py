from django.db import models
from django.conf import settings

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    participant_count = models.IntegerField(default=0)
    duration = models.IntegerField()
    test_img = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recommendation_count = models.IntegerField(default=0)
    result = models.CharField(max_length=255)