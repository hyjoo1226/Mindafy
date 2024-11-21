from rest_framework.response import Response
from rest_framework import status

from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, CustomLoginSerializer
from .models import User

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            user = User.objects.get(username=request.data['username'])
            user_data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "nickname": user.nickname,
                "age": user.age,
                "profile_img": user.profile_img,
                "created_at": user.created_at
            }
            user.save()
            return Response({
                "user": user_data,
                "key": response.data['key']
            }, status=status.HTTP_201_CREATED)

        return response

class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            user = User.objects.get(username=request.data['username'])
            user_data = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "nickname": user.nickname,
                "age": user.age,
                "profile_img": user.profile_img,
                "created_at": user.created_at
            }
            user.save()
            return Response({
                "user": user_data,
                "key": response.data['key']
            }, status=status.HTTP_200_OK)

        return response