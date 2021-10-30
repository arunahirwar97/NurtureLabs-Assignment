from django.shortcuts import render
from .models import *
from .serializers import * 
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid
from rest_framework.views import APIView

# Create your views here.
class AdvisorViewSet(APIView):
    serializer_class = AdvisorSerializer
    def post(self, request):
        serializedData = AdvisorSerializer(data=request.data)
        if serializedData.is_valid():
            serializedData.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)


