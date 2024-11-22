from django.db import models
from tests.models import Test

class Survey(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.TextField()
    question_type = models.CharField(max_length=50)

    attribute_key = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
