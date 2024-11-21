from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True)
    age = serializers.IntegerField(required=False, allow_null=True)
    email = serializers.EmailField(required=True)
    profile_img = serializers.CharField(required=False, allow_null=True)
    
    def save(self, request):
        user = super().save(request)
        user.nickname = self.validated_data['nickname']
        user.age = self.validated_data['age']
        user.email = self.validated_data['email']
        user.profile_img = self.validated_data['profile_img']
        user.save()

        return user
    