from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import F
from . import views
from .models import Test, Comment, Like


@api_view(['GET', 'POST'])
def test_like(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == 'GET':
        like = Like.objects.filter(user=request.user, test_id=test_id).first()
        is_like = like.is_like if like else False

        return Response({'is_like': is_like}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        like, created = Like.objects.get_or_create(user=request.user, test_id=test_id, defaults={'is_like': True})
        if created:
            Test.objects.filter(id=test_id).update(recommendation_count=F('recommendation_count') + 1)
        else:
            like.is_like = not like.is_like
            like.save()

            if like.is_like:
                Test.objects.filter(id=test_id).update(recommendation_count=F('recommendation_count') + 1)
            else:
                Test.objects.filter(id=test_id).update(recommendation_count=F('recommendation_count') - 1)
    
        return Response(like.is_like, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def comment_like(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'GET':
        like = Like.objects.filter(user=request.user, comment_id=comment_id).first()
        is_liked = like.is_like if like else False

        return Response({'is_liked': is_liked}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        like, created = Like.objects.get_or_create(user=request.user, comment_id=comment_id, defaults={'is_like': True})
        if created:
            Comment.objects.filter(id=comment_id).update(recommendation_count=F('recommendation_count') + 1)
        else:
            like.is_like = not like.is_like
            like.save()

            if like.is_like:
                Comment.objects.filter(id=comment_id).update(recommendation_count=F('recommendation_count') + 1)
            else:
                Comment.objects.filter(id=comment_id).update(recommendation_count=F('recommendation_count') - 1)
        
        return Response(like.is_like, status=status.HTTP_200_OK)
