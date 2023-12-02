from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Chat
from .serializers import ChatSerializer
from .external_tools import generate_response
from users.models import CustomUser


@api_view(["POST"])
def send_question(request):
    user_id = request.data.get("user")
    question_text = request.data.get("question_text")
    answer_text = generate_response(question_text)

    if not answer_text:
        answer_text = "Sorry, try again!"

    # Retrieve the CustomUser instance based on the user ID
    user = CustomUser.objects.get(id=user_id)

    # Create a new entry in the Chat table
    chat = Chat.objects.create(
        user=user,
        question_text=question_text,
        answer_text=answer_text,
    )

    # Use the ChatSerializer for response, passing the chat instance
    serializer = ChatSerializer(chat)

    return Response({"chat": serializer.data}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def chat_list(request):
    user_id = request.query_params.get("user")
    user = CustomUser.objects.get(id=user_id)

    chats = Chat.objects.filter(user=user)
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)
