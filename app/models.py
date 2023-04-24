from django.db import models

# Create your models here.
class Supplier(models.Model):
    supplier = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    stateRegistration = models.IntegerField()
    telephone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)