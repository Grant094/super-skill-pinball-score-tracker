from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "sspscoresapp/index.html")

class ScoresListView(ListView):
    model = Score
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ScoreCreate(CreateView):
    model = Score
    form_class = ScoreCreateForm
    template_name = "sspscoresapp/score_create_form.html"

    def get_initial(self):
        self.initial.update({ 'player' : self.request.user })
        return self.initial