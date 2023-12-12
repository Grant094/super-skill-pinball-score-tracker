from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("scores/", ScoresListView.as_view(), name="scores-list"),
]