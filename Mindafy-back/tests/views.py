from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Test
from .serializers import TestSerializer

@api_view(['GET'])
def tests(request):
    tests = get_list_or_404(Test)
    serializer = TestSerializer(tests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def test_detail(request, test_pk):
    test = get_object_or_404(Test, pk=test_pk)
    serializer = TestSerializer(test)
    return Response(serializer.data)