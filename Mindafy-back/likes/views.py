from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import F
from . import views
from .models import Test, Comment, Like


@api_view(['POST', 'DELETE'])
def test_like(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    like = Like.objects.filter(user=request.user, test_id=test_id)
    if request.method == 'POST':
        if not like:
            Like.objects.create(user=request.user, test_id=test_id)
            Test.objects.filter(id=test_id).update(recommendation_count=F('recommendation_count') + 1)
            return Response(status=status.HTTP_201_CREATED)
        return Response({'error': '이미 좋아요를 눌렀습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if like:
            like.delete()
            Test.objects.filter(id=test_id).update(recommendation_count=F('recommendation_count') - 1)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': '좋아요를 누르지 않았습니다.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'DELETE'])
def comment_like(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    like = Like.objects.filter(user=request.user, comment_id=comment_id)
    if request.method == 'POST':
        if not like:
            Like.objects.create(user=request.user, comment_id=comment_id)
            Comment.objects.filter(id=comment_id).update(recommendation_count=F('recommendation_count') + 1)
            return Response(status=status.HTTP_201_CREATED)
        return Response({'error': '이미 좋아요를 눌렀습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        if like:
            like.delete()
            Comment.objects.filter(id=comment_id).update(recommendation_count=F('recommendation_count') - 1)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': '좋아요를 누르지 않았습니다.'}, status=status.HTTP_400_BAD_REQUEST)
