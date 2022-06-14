from django.contrib import admin
from pinceru_games.models import Game, Genre

class Games(admin.ModelAdmin):
    list_display = ('id', 'name', 'release_date', 'rating',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'gender', 'rating',)
    list_filter = ('rating',)
    list_per_page = 10
    ordering = ('release_date',)

class Genres(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Game, Games)
admin.site.register(Genre, Genres)

