from django.db import models
from users.models import CustomUser


class UserMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.timestamp}"


class BotResponse(models.Model):
    user_message = models.ForeignKey(UserMessage, on_delete=models.CASCADE)
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.user_message.user_id} - {self.timestamp}"
