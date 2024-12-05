from rest_framework import serializers
from django.conf import settings
from .models import Test, TestResult


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
    
    def get_test_img(self, obj):
        if obj.test_img:
            request = self.context.get('request')
            img_path = obj.test_img
            return request.build_absolute_uri(settings.STATIC_URL + img_path)
        return None

class TestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestResult
        fields = '__all__'