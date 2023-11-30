from django.db import models
from users.models import CustomUser


class InsulinType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class InsulinTake(models.Model):
    units = models.FloatField()
    insulin_type = models.ForeignKey(InsulinType, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Insulin Entry - {self.units} units"
