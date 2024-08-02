from rest_framework import serializers
from apps.resources.models import Iron

class IronSerializer(serializers.ModelSerializer):
    current_iron = serializers.SerializerMethodField()

    class Meta:
        model = Iron
        fields = ('id', 'quantity', 'current_iron')

    def get_current_iron(self, obj):
        return obj.get_current_iron()