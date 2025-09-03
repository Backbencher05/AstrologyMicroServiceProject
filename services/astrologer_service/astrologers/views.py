from django.shortcuts import render
from rest_framework import generics
from .models import Astrologer
from .serializers import AstrologerSerializer

# Create your views here.

class AstrologerListCreateView(generics.ListCreateAPIView):
    queryset = Astrologer.objects.all()
    serializer_class = AstrologerSerializer