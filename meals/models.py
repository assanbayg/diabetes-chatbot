from django.db import models
from users.models import CustomUser


class Meal(models.Model):
    name = models.CharField(max_length=255)
    portion_size = models.FloatField()
    kcal = models.FloatField()
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Meal - {self.name}"


class NutritionHistory(models.Model):
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name="nutrition_history"
    )
    date = models.DateTimeField(auto_now_add=True)
    blood_sugar_before = models.FloatField(null=True, blank=True)
    blood_sugar_after = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Nutrition History - {self.meal.name} ({self.date})"
