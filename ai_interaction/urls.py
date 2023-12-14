from django.urls import path
from .views import chat_list, send_question

urlpatterns = [
    path("chats/<int:pk>", chat_list, name="chat-list"),
    path("send_question/", send_question, name="send-question"),
]