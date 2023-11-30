from django.db import models
from users.models import CustomUser


class BloodLevelEntry(models.Model):
    level = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"Blood Level Entry - {self.id}"
