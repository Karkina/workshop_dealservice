from django.db import models

# Create your models here.


class Provider(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    montant = models.CharField(max_length=100000000)
    zone = models.CharField(max_length=10)
    devise = models.CharField(max_length=20)
    brower = models.CharField(max_length=100)
    lender = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
