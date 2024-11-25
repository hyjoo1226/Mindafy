from django.db import models
from accounts.models import User
from finance.models import DepositProducts, SavingProducts, EtfProducts

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    deposit_product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, null=True, blank=True)
    saving_product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE, null=True, blank=True)
    etf_product = models.ForeignKey(EtfProducts, on_delete=models.CASCADE, null=True, blank=True)
    attribute_key = models.CharField(max_length=100, default='default')
    attribute_value = models.TextField()
    result = models.TextField(default='default')
    result_img = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)