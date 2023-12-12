from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
    SOLO = "SOLO"
    FFA2P = "FFA2P" # FREE-FOR-ALL TWO-PLAYER
    FFA3P = "FFA3P" # FREE-FOR-ALL THREE-PLAYER
    FFA4P = "FFA4P" # FREE-FOR-ALL FOUR-PLAYER
    COOP2P = "COOP2P" # COOPERATIVE TWO-PLAYER
    VARIANT_CHOICES = (
        (SOLO, 'Solo'),
        (FFA2P, 'Free-for-All Two-Player'),
        (FFA3P, 'Free-for-All Three-Player'),
        (FFA4P, 'Free-for-All Four-Player'),
        (COOP2P, 'Cooperative Two-Player'),
    )

    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    pin = models.ForeignKey('Pin', on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    variant = models.CharField(max_length=6, choices=VARIANT_CHOICES, default=SOLO)

    def __str__(self):
        return str(self.score) + " on " + str(self.pin) + " at " + str(self.timestamp) + " by " + str(self.player)
    
    def get_absolute_url(self):
        return reverse('scores-list')
    
class Pin(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

