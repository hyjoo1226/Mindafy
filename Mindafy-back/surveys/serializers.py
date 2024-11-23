from rest_framework import serializers
from .models import Survey, SurveyAnswer, SurveyOption, SurveyQuestion


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'