from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import DepositProducts, DepositOptions, SavingProducts, EtfProducts, SavingOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, EtfProductsSerializer, SavingOptionsSerializer

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

        deposit_product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)

        product_options = [
            option for option in response['result']['optionList'] 
            if option['fin_prdt_cd'] == fin_prdt_cd
        ]

        for option in product_options:
            DepositOptions.objects.get_or_create(
                product=deposit_product,
                save_trm=option['save_trm'],
                intr_rate=option['intr_rate'],
                intr_rate2=option['intr_rate2']
            )

    
    return JsonResponse({'message': '예금 데이터 저장'})


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

        saving_product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)

        product_options = [
            option for option in response['result']['optionList'] 
            if option['fin_prdt_cd'] == fin_prdt_cd
        ]

        for option in product_options:
            SavingOptions.objects.get_or_create(
                product=saving_product,
                save_trm=option['save_trm'],
                intr_rate=option['intr_rate'],
                intr_rate2=option['intr_rate2'],
                rsrv_type_nm=option['rsrv_type_nm'],
                intr_rate_type_nm=option['intr_rate_type_nm']
            )
    
    return JsonResponse({'message': '적금 데이터 저장'})

@api_view(['GET'])
@permission_classes([AllowAny])
def save_etf(request):
    api_key = settings.ETF_API_KEY
    url = f'https://apis.data.go.kr/1160100/service/GetSecuritiesProductInfoService/getETFPriceInfo?serviceKey={api_key}&numOfRows=10000&pageNo=1&resultType=json'
    response = requests.get(url).json()
    items = response['response']['body']['items']['item']
    for item in items:
        itmsNm = item['itmsNm']
        fltRt = item['fltRt']
        trqu = item['trqu']
        bssIdxIdxNm = item['bssIdxIdxNm']

        if EtfProducts.objects.filter(itmsNm=itmsNm, fltRt=fltRt, trqu=trqu, bssIdxIdxNm=bssIdxIdxNm).exists():
            continue

        save_data = {
            'itmsNm': itmsNm,
            'fltRt': fltRt,
            'trqu': trqu,
            'bssIdxIdxNm': bssIdxIdxNm,
        }

        serializer = EtfProductsSerializer(data = save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return JsonResponse({'message': 'ETF 데이터 저장'})