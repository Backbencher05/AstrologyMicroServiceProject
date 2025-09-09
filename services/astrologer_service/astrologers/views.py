from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Astrologer
from .serializers import AstrologerSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# class AstrologerListCreateView(generics.ListCreateAPIView):
#     queryset = Astrologer.objects.all()
#     serializer_class = AstrologerSerializer

class AstrologerViewSet(viewsets.ModelViewSet):
    queryset = Astrologer.objects.all()
    serializer_class = AstrologerSerializer
    permission_classes = [IsAuthenticated]




from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def whoami(request):
    # AccessToken object → get raw payload
    claims = getattr(request.auth, "payload", {}) or {}

    return Response({
        "user_id": claims.get("user_id"),
        "is_authenticated": request.user.is_authenticated,
        "claims": claims,
    })