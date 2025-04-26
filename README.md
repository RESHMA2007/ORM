# Ex02 Django ORM Web Application
## Date: 26.04.2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![Screenshot 2025-04-26 154526](https://github.com/user-attachments/assets/7799cd62-e58d-407b-9899-e832b789459e)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Movie, MovieAdmin
admin.site.register(Movie, MovieAdmin)

models.py

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
```


## OUTPUT
![alt text](<Screenshot 2025-04-26 152740.png>)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
