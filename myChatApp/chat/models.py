from django.db import models
from django_countries.fields import CountryField



# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    interest = models.CharField(max_length=50)
    countries = CountryField()
    #countryChosen = models.CharField(
    #    max_length=2,
     #   choices=countries,
      #  default="United States",
    #)

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
    )
   
