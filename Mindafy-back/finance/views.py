from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import DepositProducts, DepositOptions, SavingProducts
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer

# 예금 데이터 DB 저장
@api_view(['GET'])
@permission_classes([AllowAny])
def save_deposit(request):
    api_key = settings.FINANCE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for item in response['result']['baseList']:
        fin_prdt_cd = item['fin_prdt_cd']
        kor_co_nm = item['kor_co_nm']
        fin_prdt_nm = item['fin_prdt_nm']
        mtrt_int = item['mtrt_int']
        spcl_cnd = item['spcl_cnd']
        etc_note = item['etc_note']

        if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd, kor_co_nm=kor_co_nm, fin_prdt_nm=fin_prdt_nm, mtrt_int=mtrt_int, spcl_cnd=spcl_cnd, etc_note=etc_note).exists():
            continue
        
        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'mtrt_int': mtrt_int,
            'etc_note': etc_note,
            'spcl_cnd': spcl_cnd,
            'etc_note': etc_note
        }

        serializer = DepositProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return JsonResponse({'message': '예금 데이터 저장'})

# 예금 데이터 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def deposit(request):
    pass

# 적금 데이터 DB 저장
@api_view(['GET'])
@permission_classes([AllowAny])
def save_saving(request):
    api_key = settings.FINANCE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for item in response['result']['baseList']:
        fin_prdt_cd = item['fin_prdt_cd']
        kor_co_nm = item['kor_co_nm']
        fin_prdt_nm = item['fin_prdt_nm']
        mtrt_int = item['mtrt_int']
        spcl_cnd = item['spcl_cnd']
        etc_note = item['etc_note']

        if SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd, kor_co_nm=kor_co_nm, fin_prdt_nm=fin_prdt_nm, mtrt_int=mtrt_int, spcl_cnd=spcl_cnd, etc_note=etc_note).exists():
            continue
        
        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'mtrt_int': mtrt_int,
            'etc_note': etc_note,
            'spcl_cnd': spcl_cnd,
            'etc_note': etc_note
        }

        serializer = SavingProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return JsonResponse({'message': '적금 데이터 저장'})