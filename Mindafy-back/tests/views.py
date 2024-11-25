from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


from django.shortcuts import get_list_or_404, get_object_or_404
import json
from django.db.models import F, Func
from surveys.models import SurveyAnswer, SurveyOption, SurveyQuestion
from .models import Test, TestResult
from finance.models import DepositProducts, SavingProducts, EtfProducts
from .serializers import TestSerializer, TestResultSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def tests(request):
    tests = get_list_or_404(Test)
    serializer = TestSerializer(tests, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    serializer = TestSerializer(test)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_test_result(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    test_result = {
        'user': request.user.id if request.user.is_authenticated else None,
        'test': test_id,
        'attribute_key': 'default',
        'attribute_value': 0,
        'result': 'default',
        'result_img': None
    }
    serializer = TestResultSerializer(data=test_result)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        Test.objects.filter(id=test_id).update(participant_count=F('participant_count') + 1)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def test_results(request):
    test_results = TestResult.objects.filter(user_id=request.user.id)
    serializer = TestResultSerializer(test_results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def test_result_detail(request, test_result_id):
    test_result = get_object_or_404(TestResult.objects.select_related('user', 'test'), id=test_result_id)
    serializer = TestResultSerializer(test_result)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def calculate_test1_result(request, test_result_id):
    test_result = get_object_or_404(TestResult, id=test_result_id)
    survey1_answers = SurveyAnswer.objects.filter(test_result_id=test_result_id, question__survey_id=1).order_by('question__question_number')

    risk_aversion_scores = [int(answer.answer_value) for answer in survey1_answers if answer.question.question_number % 2 != 0]
    stimulus_seeking_scores = [int(answer.answer_value) for answer in survey1_answers if answer.question.question_number % 2 == 0]
    
    risk_total = sum(risk_aversion_scores)
    stimulus_total = sum(stimulus_seeking_scores)
 
    def categorize_score(score):
        if score <= 35:
            return 'LOW'
        elif score <= 70:
            return 'MEDIUM'
        else:
            return 'HIGH'
        
    risk_category = categorize_score(risk_total)
    stimulus_category = categorize_score(stimulus_total)

    result_matrix = {
        ('LOW', 'LOW'): '위험회피L자극추구L',
        ('LOW', 'MEDIUM'): '위험회피L자극추구M',
        ('LOW', 'HIGH'): '위험회피L자극추구H',
        ('MEDIUM', 'LOW'): '위험회피M자극추구L',
        ('MEDIUM', 'MEDIUM'): '위험회피M자극추구M',
        ('MEDIUM', 'HIGH'): '위험회피M자극추구H',
        ('HIGH', 'LOW'): '위험회피H자극추구L',
        ('HIGH', 'MEDIUM'): '위험회피H자극추구M',
        ('HIGH', 'HIGH'): '위험회피H자극추구H'
    }
    
    def determine_type(result):
        special_types = [
            '위험회피L자극추구L',
            '위험회피M자극추구L',
            '위험회피H자극추구L',
            '위험회피H자극추구M'
        ]
        return '저위험' if result in special_types else '고위험'
    
    psy_result = result_matrix[(risk_category, stimulus_category)]
    psy_type = determine_type(psy_result)
    is_match = False


    survey2_answers = SurveyAnswer.objects.filter(test_result_id=test_result_id, question__survey_id=2).select_related('question').order_by('question__question_number')

    option_scores = {
    '1': 4,  # 1번보기: 4점
    '2': 3,  # 2번보기: 3점
    '3': 2,  # 3번보기: 2점
    '4': 1   # 4번보기: 1점
    }   
    score_sum = sum(
    option_scores[answer.answer_value] 
    for answer in survey2_answers[:2]
    )

    q3_value = survey2_answers[2].answer_value

    q4_answer = survey2_answers[3]

    question = SurveyQuestion.objects.get(id=q4_answer.question.id)
    # q4_option = question.options.get(option_number=q4_answer.answer_value)
    
    #2
    # q4_option = SurveyOption.objects.get(
    #     question_id=q4_answer.question.id,  # 올바른 필드 이름
    #     option_number=q4_answer.answer_value
    # )

    #3
    q4_option = SurveyOption.objects.get(
    question=q4_answer.question,  # SurveyQuestion FK 관계
    option_number=q4_answer.answer_value
    )


    selected_bank = q4_option.option_text

    if q3_value == '1':
        deposits = DepositProducts.objects.filter(kor_co_nm__in=selected_bank)
        test_result.deposit_product = deposits.first()
        test_result.saving_product = None
        test_result.etf_product = None
        # test_result.investment_product = None
        products_data = deposits
        if psy_type == '저위험':
            is_match = True

    elif q3_value == '2':
        savings = SavingProducts.objects.filter(kor_co_nm__in=selected_bank)
        test_result.deposit_product = None
        test_result.saving_product = savings.first()
        test_result.etf_product = None
        products_data = savings
        if psy_type == '저위험':
            is_match = True
        # test_result.investment_product = None
    elif q3_value == '3':
        if score_sum >= 6:
            etfs = EtfProducts.objects.filter(
            trqu__gte=1000000  # 거래량이 100만 이상
            ).annotate(
                abs_fltRt=Func(F('fltRt'), function='ABS')  # 등락률의 절댓값 계산
            ).order_by('-abs_fltRt')[:5]  # 절댓값 기준 내림차순 정렬
            test_result.deposit_product = None
            test_result.saving_product = None
            test_result.etf_product = etfs.fitst()
            products_data = etfs
            if psy_type == '고위험':
                is_match = True
        else:
        # ETF/펀드 데이터
            pass
        # test_result.deposit_product = None
        # test_result.saving_product = None
        # test_result.investment_product = investment.first()


    attribute_data = {
        'psy_result': psy_result,
        'risk_total': risk_total,
        'stimulus_total': stimulus_total,
        'is_match': is_match,
        'products': list(products_data.values())
    }

    result_data = {
        'products': list(products_data.values())
    }
    
    test_result.attribute_key = 'test1_results'
    test_result.attribute_value = json.dumps(attribute_data)
    # test_result.result = json.dumps(result_data) 새로운결과값
    test_result.save()

    return Response({
        **attribute_data,
        **result_data
    }, status=status.HTTP_200_OK)


    # response_data = {
    #     'products': list(products_data.values()),
    #     'result': psy_result,
    #     'risk_total': risk_total,
    #     'stimulus_total': stimulus_total,
    #     'is_match': is_match
    # }



    # test_result.result = json.dumps(response_data)
    # test_result.save()

    # return Response(response_data, status=status.HTTP_200_OK)


    # return Response({
    #     'products': products_data.values(),
    #     'result': psy_result,
    #     'risk_total': risk_total,
    #     'stimulus_total': stimulus_total,
    #     'is_match': is_match
    # }, status=status.HTTP_200_OK)