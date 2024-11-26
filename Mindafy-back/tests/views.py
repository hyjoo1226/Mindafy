from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_list_or_404, get_object_or_404
import json
from django.db.models import F, Func
from surveys.models import SurveyAnswer, SurveyOption, SurveyQuestion
from .models import Test, TestResult
from finance.models import DepositProducts, SavingProducts, EtfProducts, DepositOptions, SavingOptions
from .serializers import TestSerializer, TestResultSerializer
from finance.serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingOptionsSerializer, SavingProductsSerializer

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
    
    def psy_result_description(psy_result):
        descriptions = {
            '위험회피L자극추구L': '차분하고 자신감 있는 당신은 어떤 상황에서도 흔들리지 않는 안정적인 성격을 가지고 있습니다. 예상치 못한 변화나 도전적인 상황에서도 스트레스를 받기보다는 침착하게 대응하며, 여유를 잃지 않습니다. 주변 사람들은 당신의 이런 태도에서 안정감과 신뢰를 느낄 수 있습니다.',
            '위험회피L자극추구M': '새로운 경험에 대해 열린 태도를 가진 당신은 적당한 모험심과 균형 잡힌 태도를 모두 가지고 있습니다. 도전적인 상황에서도 지나치게 긴장하지 않으며, 변화를 자연스럽게 받아들입니다. 당신은 단조로운 일상에서 벗어나고자 하면서도 무모한 선택은 피하려는 지혜로운 사람입니다.',
            '위험회피L자극추구H': '당신은 모험심이 강하고 변화와 도전을 즐기는 자유로운 영혼입니다. 새로운 환경에서 흥미를 느끼며, 위험이 따르더라도 이를 두려워하지 않습니다. 새로운 프로젝트나 모험적인 활동에 적극적으로 참여하며, 주변 사람들에게 활력을 불어넣는 성격입니다.',
            '위험회피M자극추구L': '당신은 안정적이면서도 새로운 것에 대한 호기심을 완전히 배제하지 않는 균형 잡힌 성격을 가지고 있습니다. 위험한 상황에서는 신중하게 판단하지만, 지나치게 방어적으로 행동하지도 않습니다. 필요할 때는 적절히 결단을 내리며, 안정과 도전 사이의 절묘한 균형을 유지합니다.',
            '위험회피M자극추구M': '당신은 모든 상황에서 위험과 보상을 동시에 고려하는 신중하면서도 도전적인 태도를 가졌습니다. 새로운 환경이나 기회를 환영하면서도, 항상 안전성을 중요하게 생각합니다. 이는 당신의 대인 관계나 업무에서 매우 유리하게 작용할 수 있습니다.',
            '위험회피M자극추구H': '높은 모험심과 더불어 안전을 추구하려는 경향을 동시에 가진 당신. 새로운 기회를 탐색하면서도 결과를 예상하고 리스크를 조절하려는 균형 잡힌 태도를 보입니다. 당신은 모험을 즐기되, 자신에게 무리가 가지 않도록 항상 최적의 상태를 유지하려 노력합니다.',
            '위험회피H자극추구L': '새로운 상황이나 변화 앞에서는 긴장과 불안을 느끼기 쉬운 당신. 보수적이고 신중한 태도를 유지하며, 위험을 최소화하기 위해 많은 노력을 기울입니다. 변화보다는 익숙한 환경에서 안정을 추구하며, 도전적인 일을 선택하기보다는 확실한 결과를 보장받을 수 있는 일을 선호합니다.',
            '위험회피H자극추구M': '자극 추구 성향이 중간임에도 불구하고, 안전을 중요시하는 당신은 새로운 환경이나 변화 앞에서 항상 조심스럽게 접근합니다. 호기심이 많지만, 불확실한 상황에서는 신중한 태도를 유지하며, 작은 리스크도 면밀히 분석하려는 경향이 있습니다.',
            '위험회피H자극추구H': '당신은 새로운 경험에 끌리면서도 불안을 느끼는 모순된 경향을 보입니다. 흥미로운 일이 있어도 잠재적인 위험 때문에 망설이는 경우가 많으며, 안전한 조건에서만 모험을 시도하려는 특징이 있습니다. 이러한 성향은 때로 자신을 보호하는 데 유리하지만, 도전의 기회를 놓칠 수도 있습니다.',
        }
        return descriptions.get(psy_result)
    
    def psy_result_type(psy_result):
        types = {
            '위험회피L자극추구L': '"조금의 변화도 흔들리지 않는 안정형!"',
            '위험회피L자극추구M': '"도전과 안정의 조화! 개방형!"',
            '위험회피L자극추구H': '"세상은 넓고 할 건 많다! 탐험형!"',
            '위험회피M자극추구L': '"안정과 신중 사이의 완벽한 중재자형!"',
            '위험회피M자극추구M': '"신중하지만 도전도 즐기는 균형형!"',
            '위험회피M자극추구H': '"모험도, 안전도! 조화로운 탐구형!"',
            '위험회피H자극추구L': '"안전이 제일 중요! 조심형!"',
            '위험회피H자극추구M': '"호기심 많은 안전주의형!"',
            '위험회피H자극추구H': '"모순 속의 균형! 불안한 도전형!"',
        }
        return types.get(psy_result)

    
    psy_result = result_matrix[(risk_category, stimulus_category)]
    description = psy_result_description(psy_result)
    result_type = psy_result_type(psy_result)
    psy_type = psy_result_type(psy_result)
    match = '자극추구와 위험회피 성향을 분석한 결과, 투자 목적과 약간의 차이가 있습니다.'


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
    q4_option = SurveyOption.objects.get(question=q4_answer.question, option_number=q4_answer.answer_value)
    selected_bank = q4_option.option_text


    
    if q3_value == '1':
        deposits = DepositProducts.objects.filter(kor_co_nm=selected_bank)
        deposits_with_options = []
        for deposit in deposits:
            deposit_serializer = DepositProductsSerializer(deposit)

            options = DepositOptions.objects.filter(product=deposit)
            options_serializer = DepositOptionsSerializer(options, many=True)
            
            deposit_data = {
                'product': deposit_serializer.data,
                'options': options_serializer.data
            }
            deposits_with_options.append(deposit_data)

        test_result.deposit_product = deposits.first()
        test_result.saving_product = None
        test_result.etf_product = None
        # test_result.investment_product = None
        products_data = deposits_with_options
        if psy_type == '저위험':
            match = '자극추구와 위험회피 성향을 분석한 결과, 투자 목적과 일치합니다.'

    elif q3_value == '2':
        savings = SavingProducts.objects.filter(kor_co_nm=selected_bank)
        savings_with_options = []
        for saving in savings:
            saving_serializer = SavingProductsSerializer(saving)

            options = SavingOptions.objects.filter(product=saving)
            options_serializer = SavingOptionsSerializer(options, many=True)

            saving_data = {
                'product': saving_serializer.data,
                'options': options_serializer.data
            }
            savings_with_options.append(saving_data)
        test_result.deposit_product = None
        test_result.saving_product = savings.first()
        test_result.etf_product = None
        products_data = savings_with_options
        if psy_type == '저위험':
            match = '자극추구와 위험회피 성향을 분석한 결과, 투자 목적과 일치합니다.'
        # test_result.investment_product = None
    elif q3_value == '3':
        # if score_sum >= 6:
            etfs = EtfProducts.objects.filter(
            trqu__gte=1000000  # 거래량이 100만 이상
            ).annotate(
                abs_fltRt=Func(F('fltRt'), function='ABS')  # 등락률의 절댓값 계산
            ).order_by('-abs_fltRt')[:5]  # 절댓값 기준 내림차순 정렬
            test_result.deposit_product = None
            test_result.saving_product = None
            test_result.etf_product = etfs.first()
            products_data = etfs
            if psy_type == '고위험':
                match = '자극추구와 위험회피 성향을 분석한 결과, 투자 목적과 일치합니다.'
        # ETF/펀드 데이터
        # else:
        #     pass
        # test_result.deposit_product = None
        # test_result.saving_product = None
        # test_result.investment_product = investment.first()


    attribute_data = {
        'psy_result': psy_result,
        'risk_total': risk_total,
        'stimulus_total': stimulus_total,
        'match': match,
        'result_type': result_type,
        'description': description,
        'products': products_data
        # 'products': list(products_data.values())
    }

    # result_data = {
    #     'products': list(products_data.values())
    # }
    
    test_result.attribute_key = 'test1_results'
    test_result.attribute_value = json.dumps(attribute_data, cls=DjangoJSONEncoder)
    # test_result.result = json.dumps(result_data) 새로운결과
    test_result.save()

    return Response({
        **attribute_data
        # **result_data
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