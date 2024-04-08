from django.urls import path

from testing_app.views import SingerView, SongView

urlpatterns = [
    path("singer/", SingerView.as_view()),
    path("song/", SongView.as_view()),
]
