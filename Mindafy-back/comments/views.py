from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Comment, Test
from .serializers import CommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

@api_view(['GET'])
@permission_classes([AllowAny])
def comments(request, test_id=None):
    if test_id:
        test = get_object_or_404(Test, id=test_id)
        comments = test.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def comment_detail(request, comment_id):
    comments = get_object_or_404(Comment, id=comment_id)
    serializer = CommentSerializer(comments)
    return Response(serializer.data, status=status.HTTP_200_OK)