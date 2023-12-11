from django.db import models

# Create your models here.
class Score(models.Model):
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    pin = models.ForeignKey('Pin', on_delete=models.CASCADE)

class Pin(models.Model):
    name = models.CharField(max_length=200)