from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    RATING = (
        ('RP', 'Classificação Pendente'),
        ('EC', 'Primeira Infância'),
        ('E', 'Todos'),
        ('E10+', 'Todos com mais de 10 anos'),
        ('T', 'Adolescente'),
        ('M', 'Maduro'),
        ('A', 'Adulto')
    )
    name = models.CharField(max_length=100, blank=False, null=False)
    release_date = models.DateField()
    rating = models.CharField(blank=False, null=False, max_length=4, choices=RATING)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

    
