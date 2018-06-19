from django.db import models


# Create your models here.
class ContractManager(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=15)


class Section(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()


class Company(models.Model):
    name = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=15)


class Contract(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    section = models.ForeignKey('Section', on_delete=models.DO_NOTHING)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    start_date = models.DateField()
    expiry_date = models.DateField()
    contract_manager = models.ForeignKey('ContractManager', on_delete=models.DO_NOTHING)

