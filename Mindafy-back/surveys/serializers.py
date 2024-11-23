from rest_framework import serializers
from .models import Survey, SurveyAnswer, SurveyOption, SurveyQuestion


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'

class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = '__all__'