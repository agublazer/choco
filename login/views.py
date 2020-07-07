from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    fecha_inicio = models.DateField(default=date.today)
    fecha_fin = models.DateField(default=date.today)

    def __str__(self):
        return str(self.user.get_username())


class Package(models.Model):
    months = models.IntegerField(default=0)
    price = models.FloatField(default=0)
