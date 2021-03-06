# Generated by Django 4.0.5 on 2022-06-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('registration_date', models.DateField()),
                ('rating', models.CharField(choices=[('RP', 'Classificação Pendente'), ('EC', 'Primeira Infância'), ('E', 'Todos'), ('E10+', 'Todos com mais de 10 anos'), ('T', 'Adolescente'), ('M', 'Maduro'), ('A', 'Adulto')], max_length=4)),
                ('genre', models.ManyToManyField(to='pinceru_games.genre')),
            ],
        ),
    ]
