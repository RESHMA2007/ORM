from django.db import models
from django.contrib import admin

class Movie(models.Model):
    Moviename = models.CharField(max_length=100)
    Actor = models.CharField(max_length=100)
    Genre = models.CharField(max_length=50) 
    Rating = models.FloatField()
    Releaseyear = models.IntegerField()

    def __str__(self):
        return self.Moviename

class MovieAdmin(admin.ModelAdmin):
    list_display = ('Moviename', 'Actor', 'Genre', 'Rating', 'Releaseyear')

