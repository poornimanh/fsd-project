from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Coffee(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    quantity=models.IntegerField()
    image=models.CharField(max_length=2083)

    # models.py


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
