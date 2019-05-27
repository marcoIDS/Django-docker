from django.urls import path
from .views import ListSongsView


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('songs/<int:pk>', ListSongsView.as_view(), name="songs-all")
]   