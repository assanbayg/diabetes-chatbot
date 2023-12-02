from django.urls import path
from .views import chat_list, send_question

urlpatterns = [
    path("chats/", chat_list, name="chat-list"),
    path("send_query/", send_question, name="send-question"),
]
