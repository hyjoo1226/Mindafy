from rest_framework.response import Response

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True)
    age = serializers.IntegerField(required=False, allow_null=True)
    email = serializers.EmailField(required=True)
    profile_img = serializers.CharField(required=False, allow_null=True)
    

    def validate_age(self, age):
        if age <= 0 or age > 200:
             raise serializers.ValidationError("나이를 올바르게 입력해주세요.")
        return age

    def save(self, request):
        user = super().save(request)
        user.nickname = self.validated_data['nickname']
        user.age = self.validated_data['age']
        user.email = self.validated_data['email']
        user.profile_img = self.validated_data['profile_img']
        user.save()

        return user

class CustomLoginSerializer(LoginSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'