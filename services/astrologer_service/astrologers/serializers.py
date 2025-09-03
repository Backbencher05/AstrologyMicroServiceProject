from rest_framework import serializers
from .models import Astrologer

class AstrologerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Astrologer
        fields = '__all__'
