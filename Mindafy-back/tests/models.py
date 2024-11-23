from django.db import models
from accounts.models import User

class Test(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    participant_count = models.IntegerField(default=0)
    duration = models.IntegerField()
    test_img = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recommendation_count = models.IntegerField(default=0)

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    attribute_key = models.CharField(max_length=100)
    attribute_value = models.IntegerField()
    result = models.TextField()
    result_img = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)