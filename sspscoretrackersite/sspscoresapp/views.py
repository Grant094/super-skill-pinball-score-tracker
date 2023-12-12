from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
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