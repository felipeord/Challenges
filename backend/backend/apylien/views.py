from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from .serializers import TextualcontentSerializer, UserSerializer
from .models import Textualcontent, CustomUser


class TextualcontentViewSet(viewsets.ModelViewSet):
    queryset = Textualcontent.objects.all()
    serializer_class = TextualcontentSerializer

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
