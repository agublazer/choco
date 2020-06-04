from django.db import models


class Package(models.Model):
    months = models.IntegerField(default=0)
    price = models.FloatField(default=0)
