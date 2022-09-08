from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Car(models.Model):
    name = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year = models.DateField()
    engine = models.FloatField()
    color = models.CharField(max_length=150)
    number = models.CharField(max_length=10, unique=True, null=True)


class CarImage(models.Model):
    image = models.ImageField(upload_to="cars", max_length=255)
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            related_name='car_images'
                            )


class CarOwner(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)



