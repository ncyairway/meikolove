from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet
from . import views
router = DefaultRouter()
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', views.upload_song, name='upload_song'),
    path('music-list/', views.music_list, name='music_list'),
]
