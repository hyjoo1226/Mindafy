from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from rest_framework.decorators import authentication_classes
# from rest_framework.decorators import permission_classes
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# @authentication_classes([TokenAuthentication])    인증해야 접근 가능하도록
# @permission_classes([IsAuthenticated])

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Test
from .serializers import TestSerializer

@api_view(['GET'])
def tests(request):
    tests = get_list_or_404(Test)
    serializer = TestSerializer(tests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    serializer = TestSerializer(test)
    return Response(serializer.data)