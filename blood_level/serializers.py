from rest_framework import serializers
from .models import BloodLevelEntry


class BloodLevelEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodLevelEntry
        fields = ["id", "level", "timestamp"]
