from rest_framework import serializers
from .models import Meal, NutritionHistory


class MealSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()    

    class Meta:
        model = Meal
        fields = [
            "id",
            "name",
            "portion_size",
            "kcal",
            "carbs",
            "proteins",
            "fats",
        ]


class NutritionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionHistory
        fields = ["id", "meal", "date", "blood_sugar_before", "blood_sugar_after"]
