from rest_framework import viewsets, filters, serializers
from pinceru_games.serializers import GameSerializer, GenreSerializer
from pinceru_games.models import Game, Genre
from pinceru_games.validators import *
from django_filters.rest_framework import DjangoFilterBackend

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['release_date']
    search_fields = ['name', 'gender', 'rating']
    filterset_fields = ['rating']

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']

    def validate(self, data):
        if not genre_is_valid(data['name']):
            raise serializers.ValidationError({'name':"O genero deve conter somente letras."})
        return data