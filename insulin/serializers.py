from rest_framework import serializers
from .models import InsulinTake, InsulinType


class InsulinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsulinType
        fields = ["id", "name"]
        read_only_fields = fields


class InsulinTakeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = InsulinTake
        fields = [
            "id",
            "units",
            "insulin_type",
            "timestamp",
            "user",
        ]

    def create(self, validated_data):
        return InsulinTake.objects.create(**validated_data)
