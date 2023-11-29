from rest_framework import serializers
from .models import BloodLevelEntry


class BloodLevelEntrySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = BloodLevelEntry
        fields = ["id", "level", "timestamp", "formatted_date"]

    def get_formatted_date(self, obj):
        return obj.timestamp.strftime("%A, %d %B %Y %I:%M%p")
