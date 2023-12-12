from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return HttpResponse('Hello world!')

class ScoresListView(ListView):
    model = Score
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ScoreCreate(CreateView):
    model = Score
    form_class = ScoreCreateForm
    template_name = "sspscoresapp/score_create_form.html"