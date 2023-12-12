from django.urls import path
from .views import user_list, user_detail, user_login
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("", user_list, name="user-list"),
    path("<int:pk>/", user_detail, name="user-detail"),
    path("token/", ObtainAuthToken.as_view(), name="token_obtain_pair"),
    path("login/", user_login, name="user_login"),
]
