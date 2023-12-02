from django.db import models
from users.models import CustomUser


class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)
