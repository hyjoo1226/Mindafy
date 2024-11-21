from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, CustomLoginSerializer, UserSerializer
from .models import User

from django.shortcuts import get_list_or_404, get_object_or_404

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

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_profile_img(request, user_id):
   user = get_object_or_404(User, id=user_id)
   profile_img = request.data.get('profile_img')
   if profile_img:
        user.profile_img = profile_img
        user.save()
   serializer = UserSerializer(user)
   return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_nickname(request, user_id):
    user = get_object_or_404(User, id=user_id)
    nickname = request.data.get('nickname')
    if nickname:
        user.nickname = nickname
        user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)