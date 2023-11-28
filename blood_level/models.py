from django.db import models

class BloodLevelEntry(models.Model):
  level = models.FloatField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'Blood Level Entry - {self.id}'