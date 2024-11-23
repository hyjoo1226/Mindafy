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

class SurveyOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyOption
        fields = '__all__'

class SurveyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyAnswer
        fields = '__all__'