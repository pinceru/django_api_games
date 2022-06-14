
from django.contrib import admin
from django.urls import path, include
from pinceru_games.views import GameViewSet, GenreViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('game', GameViewSet, basename='Games')
router.register('genre', GenreViewSet, basename='Genres')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
