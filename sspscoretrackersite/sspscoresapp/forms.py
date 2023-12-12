from django import forms
from .models import *

class ScoreCreateForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = "__all__"