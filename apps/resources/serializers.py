from rest_framework import serializers
from .models import Iron

class IronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iron
        fields = ('id', 'quantity')