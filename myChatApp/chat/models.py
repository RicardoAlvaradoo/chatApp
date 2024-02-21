from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField



# Create your models here.
class Person(models.Model):
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key = True,
                    )
    first_name = models.CharField(max_length=50, null = True)
    last_name = models.CharField(max_length=50, null = True)
     
    interest = models.CharField(max_length=50, null = True)
    countries = CountryField(null = True)  
    
    #countryChosen = models.CharField(
    #    max_length=2,
     #   choices=countries,
      #  default="United States",
    #   )

    language = [
    ("En", "English"),
    ("Sp", "Spanish"),
    ("Ger", "German"),
    ("Flip", "Filipino"),
    ("Jap", "Japanese"), 
    
]
    langChosen = models.CharField(
        max_length=4,
        choices=language,
        default="English",
        null = True,
    )
   
