from django.db import models
from django.urls import reverse

# Create your models here.
class Score(models.Model):
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    pin = models.ForeignKey('Pin', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.score) + " on " + str(self.pin) + " at " + str(self.timestamp)
    
    def get_absolute_url(self):
        return reverse('scores-list')
    
class Pin(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
