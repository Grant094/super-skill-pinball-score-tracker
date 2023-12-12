from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("scores/", views.ScoresListView.as_view(), name="scores-list"),
    path("scores/add/", views.ScoreCreate.as_view(), name="scorecreate"),
]