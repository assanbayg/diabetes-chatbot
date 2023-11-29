from django.urls import path
from .views import blood_level_list, blood_level_detail

urlpatterns = [
    path("entries/", blood_level_list),
    path("entries/<int:pk>/", blood_level_detail),
]
