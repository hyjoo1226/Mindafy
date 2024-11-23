from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


from django.shortcuts import get_list_or_404, get_object_or_404

from django.db.models import F
from .models import Test, TestResult
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
def test_result_detail(request, test_result_id):
    test_result = get_object_or_404(TestResult.objects.select_related('user', 'test'), id=test_result_id)
    serializer = TestResultSerializer(test_result)
    return Response(serializer.data, status=status.HTTP_200_OK)
