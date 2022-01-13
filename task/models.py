from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    seller = models.CharField(max_length=50)
    created_by = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)



    def __str__(self):
        self.name