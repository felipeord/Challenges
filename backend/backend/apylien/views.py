# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, permissions, request
from .serializers import TextualcontentSerializer, AnalysisReportSerializer, AnalysisPorUsuarioSerializer
from rest_framework.views import APIView
from .models import Textualcontent, AnalysisReport
from .models import CustomUser
from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer


class TextualcontentViewSet(viewsets.ModelViewSet):
    queryset = Textualcontent.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TextualcontentSerializer

    def create(self, request, *args, **kwargs):
        print(request.data['customuser'])
        print(request.user)
        return super().create(request)



class AnalysisReportSerializer(viewsets.ModelViewSet):
    queryset = AnalysisReport.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AnalysisReportSerializer


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CustomUserSerializer(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomUser

class AnalisisPorUsuario(generics.ListAPIView):
    queryset = AnalysisReport.objects.all()
    serializer_class = AnalysisPorUsuarioSerializer



