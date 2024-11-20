from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    
    def save(self, request):
        user = super().save(request)
        user.nickname = self.validated_data['nickname']
        user.email = self.validated_data['email']
        user.save()

        return user
    # def validate_username(self, value):
    #     if User.objects.filter(username=value).exists():
    #         raise serializers.ValidationError("이미 존재하는 아이디입니다.")
    #     return value
    
    # def validate_nickname(self, value):
    #     if User.objects.filter(nickname=value).exists():
    #         raise serializers.ValidationError("이미 존재하는 닉네임입니다.")
    #     return value
    
    # def validate_email(self, value):
    #     if User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("이미 존재하는 이메일입니다.")
    #     return value
    