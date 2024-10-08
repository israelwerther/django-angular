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
        total_seconds = int(duration.total_seconds())

        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        duration_str = ""
        if days > 0:
            duration_str += f"{days}d "
        if hours > 0 or days > 0:
            duration_str += f"{hours}h "
        
        duration_str += f"{minutes}m {seconds}s"

        return duration_str.strip()


class IronSerializer(serializers.ModelSerializer):
    current_iron = serializers.SerializerMethodField()

    class Meta:
        model = Iron
        fields = ('id', 'quantity', 'current_iron')

    def get_current_iron(self, obj):
        return obj.get_current_iron()
