from aylienapiclient import textapi
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, permissions
from .serializers import TextualcontentSerializer, AnalysisReportSerializer
from rest_framework.views import APIView
from .models import Textualcontent, AnalysisReport


class TextualcontentViewSet(viewsets.ModelViewSet):
    queryset = Textualcontent.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TextualcontentSerializer

class AnalysisReportSerializer(viewsets.ModelViewSet):
    queryset = AnalysisReport.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AnalysisReportSerializer