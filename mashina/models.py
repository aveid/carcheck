from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year = models.DateField()
    engine = models.FloatField()
    color = models.CharField(max_length=150)
    number = models.CharField(max_length=10, unique=True)

class CarImage(models.Model):
    image = models.ImageField()

