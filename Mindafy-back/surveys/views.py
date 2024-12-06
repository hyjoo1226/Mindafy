from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from django.shortcuts import get_list_or_404

from .models import Survey, SurveyQuestion, SurveyOption, SurveyAnswer

from .serializers import SurveySerializer, SurveyQuestionSerializer, SurveyOptionSerializer, SurveyAnswerSerializer


# 해당 테스트의 설문 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def surveys(request, test_id):
    surveys = get_list_or_404(Survey, test_id=test_id)
    serializer = SurveySerializer(surveys, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# 해당 설문의 질문 목록 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def survey_questions(request, survey_id):
    questions = get_list_or_404(SurveyQuestion, survey_id=survey_id)
    serializer = SurveyQuestionSerializer(questions, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# 해당 설문에서 모든 질문에 대한 추가 정보 조회(ex.객관식 보기)
@api_view(['GET'])
@permission_classes([AllowAny])
def survey_options(request, survey_id):
    options = SurveyOption.objects.filter(question__survey_id=survey_id).order_by('question__question_number', 'option_number')
    serializer = SurveyOptionSerializer(options, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# 해당 질문의 추가 정보 조회(ex.객관식 보기)
@api_view(['GET'])
@permission_classes([AllowAny])
def survey_option_detail(request, survey_id, question_id):
    options = SurveyOption.objects.filter(question__survey_id=survey_id, question_id = question_id)
    serializer = SurveyOptionSerializer(options, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def survey_answers(request, test_result_id):
    # 해당 설문의 답변 조회
    if request.method == 'GET':
        answers = SurveyAnswer.objects.filter(test_result_id=test_result_id).order_by('question__question_number')
        serializer = SurveyAnswerSerializer(answers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # 해당 설문의 답변 제출
    elif request.method == 'POST':
        answers_data = request.data.get('answers', [])
        created_answers = []
        
        for answer_data in answers_data:
            answer = {
                'test_result': test_result_id,
                'question': answer_data.get('question_id'),
                'answer_value': answer_data.get('answer_value')
            }
            serializer = SurveyAnswerSerializer(data=answer)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                created_answers.append(answer)

        return Response(created_answers, status=status.HTTP_201_CREATED)


