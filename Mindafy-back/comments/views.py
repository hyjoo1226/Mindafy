from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Comment
from .serializers import CommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

@api_view(['GET'])
@permission_classes([AllowAny])
def comments(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)