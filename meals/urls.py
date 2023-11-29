from django.urls import path
from .views import (
    meal_list,
    meal_detail,
    nutrition_history_list,
    nutrition_history_detail,
)

urlpatterns = [
    path("meals/", meal_list, name="meal-list"),
    path("meals/<int:pk>/", meal_detail, name="meal-detail"),
    path(
        "nutrition_history/",
        nutrition_history_list,
        name="nutrition-history",
    ),
    path(
        "nutrition_history/<int:pk>/",
        nutrition_history_detail,
        name="nutrition-history-detail",
    ),
]
