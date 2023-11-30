from django.urls import path
from .views import insulin_type, insulin_take, insulin_take_detail

urlpatterns = [
    path("types/", insulin_type),
    path("takes/", insulin_take),
    path("takes/<int:pk>/", insulin_take_detail),
]
