from rest_framework import serializers
from apps.resources.models import Iron, IronMine

class IronMineSerializer(serializers.ModelSerializer):
    urls = serializers.JSONField(read_only=True)
    upgrade_duration = serializers.SerializerMethodField()
    class Meta:
        model = IronMine
        fields = (
            'id', 
            'level', 
            'resources_required_for_upgrade',
            'urls',
            'upgrade_duration'
        )
    def get_upgrade_duration(self, obj):
        duration = obj.upgrade_duration()
        return str(duration)

class IronSerializer(serializers.ModelSerializer):
    current_iron = serializers.SerializerMethodField()

    class Meta:
        model = Iron
        fields = ('id', 'quantity', 'current_iron')

    def get_current_iron(self, obj):
        return obj.get_current_iron()
