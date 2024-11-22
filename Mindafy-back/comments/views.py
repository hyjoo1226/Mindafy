from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Comment, Test
from .serializers import CommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comments(request, test_id=None):
    if test_id:
        test = get_object_or_404(Test, id=test_id)
        # 해당 게시글의 전체 댓글 조회
        if request.method == 'GET':
            comments = test.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # 해당 게시글에 댓글 생성
        elif request.method == 'POST':
            if not request.user.is_authenticated:
                return Response({'error': '로그인이 필요합니다.'}, status=status.HTTP_401_UNAUTHORIZED)
            comment_data = {
                'user': request.user.id,
                'test': test_id,
                'content': request.data.get('content'),
                'parent_comment': request.data.get('parent_comment')
            }
            serializer = CommentSerializer(data=comment_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    #전체 댓글 조회
    else:
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def comment_detail(request, comment_id, test_id=None):
    # 해당 게시글의 단일 댓글 조회
    if test_id:
        test = get_object_or_404(Test, id=test_id)
        comment = get_object_or_404(test.comments, id=comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # 해당 게시글의 전체 댓글 조회
    else:
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)