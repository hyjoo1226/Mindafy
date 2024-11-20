from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status

# from django.shortcuts import get_list_or_404, get_object_or_404

from .models import User
# from .serializers import CustomRegisterSerializer


# @api_view(['POST'])
# def signup(request):
#     serializer = CustomRegisterSerializer(data=request.data)

#     if serializer.is_valid():
#         user = serializer.save(request)
#         token, 
#         return Response(user)
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            user = User.objects.get(username=request.data['username'])
            user.save()
            # print(response.data)
            # print(CustomRegisterSerializer(user).data)
            # print(User.objects.get(username=request.data['username']))
            # print(response.data)
            return Response({
                "user": CustomRegisterSerializer(user).data,
                "key": response.data['key']
            }, status=status.HTTP_201_CREATED)

        return response