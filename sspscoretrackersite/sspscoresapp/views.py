from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import *

# Create your views here.
def index(request):
    return HttpResponse('Hello world!')

class ScoresListView(ListView):
    model = Score
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
