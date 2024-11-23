from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Test, Survey, SurveyQuestion, SurveyOption, SurveyAnswer
from .serializers import SurveySerializer, SurveyQuestionSerializer, SurveyOptionSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

@api_view(['GET'])
@permission_classes([AllowAny])
def surveys(request, test_id):
    surveys = get_list_or_404(Survey, test_id=test_id)
    serializer = SurveySerializer(surveys, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def survey_questions(request, survey_id):
    questions = get_list_or_404(SurveyQuestion, survey_id=survey_id)
    serializer = SurveyQuestionSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def survey_options(request, survey_id):
    options = SurveyOption.objects.filter(question__survey_id=survey_id).order_by('question__question_number', 'option_number')
    serializer = SurveyOptionSerializer(options, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def survey_option_detail(request, survey_id, question_id):
    options = SurveyOption.objects.filter(question__survey_id=survey_id, question_id = question_id)
    serializer = SurveyOptionSerializer(options, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def comments(request, test_id=None):
#     if test_id:
#         test = get_object_or_404(Test, id=test_id)
#         # 해당 게시글의 전체 댓글 조회
#         if request.method == 'GET':
#             comments = test.comments.all()
#             serializer = CommentSerializer(comments, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         # 해당 게시글에 댓글 생성
#         elif request.method == 'POST':
#             if not request.user.is_authenticated:
#                 return Response({'error': '로그인이 필요합니다.'}, status=status.HTTP_401_UNAUTHORIZED)
#             comment_data = {
#                 'user': request.user.id,
#                 'test': test_id,
#                 'content': request.data.get('content'),
#                 'parent_comment': request.data.get('parent_comment')
#             }
#             serializer = CommentSerializer(data=comment_data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #전체 댓글 조회
#     else:
#         comments = get_list_or_404(Comment)
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET', 'PATCH', 'DELETE'])
# @permission_classes([AllowAny])
# def comment_detail(request, comment_id, test_id=None):
#     if test_id:
#         test = get_object_or_404(Test, id=test_id)
#         comment = get_object_or_404(test.comments, id=comment_id)
#         # 해당 게시글의 단일 댓글 조회
#         if request.method == 'GET':
#             serializer = CommentSerializer(comment)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         # 댓글 수정
#         elif request.method == 'PATCH':
#             if not request.user.is_authenticated:
#                 return Response({'error': '로그인이 필요합니다.'}, status=status.HTTP_401_UNAUTHORIZED)
#             elif request.user.id != comment.user.id:
#                 return Response({'error': '다른 유저의 댓글입니다.'}, status=status.HTTP_403_FORBIDDEN)
            
#             serializer = CommentSerializer(comment, data={'content': request.data.get('content')}, partial=True)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#         # 댓글 삭제
#         elif request.method == 'DELETE':
#             if not request.user.is_authenticated:
#                 return Response({'error': '로그인이 필요합니다.'}, status=status.HTTP_401_UNAUTHORIZED)
#             elif request.user.id != comment.user.id:
#                 return Response({'error': '다른 유저의 댓글입니다.'}, status=status.HTTP_403_FORBIDDEN)
            
#             comment.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     # 해당 게시글의 전체 댓글 조회
#     else:
#         comment = get_object_or_404(Comment, id=comment_id)
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data, status=status.HTTP_200_OK)