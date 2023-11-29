from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Meal, NutritionHistory
from .serializers import MealSerializer, NutritionHistorySerializer


@api_view(["GET", "POST"])
def meal_list(request):
    if request.method == "GET":
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def meal_detail(request, pk):
    meal = get_object_or_404(Meal, pk=pk)

    if request.method == "GET":
        serializer = MealSerializer(meal)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MealSerializer(meal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def nutrition_history_list(request):
    if request.method == "GET":
        nutrition_history_entries = NutritionHistory.objects.all()
        serializer = NutritionHistorySerializer(nutrition_history_entries, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = NutritionHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def nutrition_history_detail(request, pk):
    nutrition_history_entry = get_object_or_404(NutritionHistory, pk=pk)

    if request.method == "GET":
        serializer = NutritionHistorySerializer(nutrition_history_entry)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = NutritionHistorySerializer(nutrition_history_entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        nutrition_history_entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)