from django.db import models


# Create your models here.
class ContractManager(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.description


class Company(models.Model):

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    name = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Contract(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    section = models.ForeignKey('Section', on_delete=models.DO_NOTHING)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    start_date = models.DateField()
    expiry_date = models.DateField()
    contract_manager = models.ForeignKey('ContractManager', on_delete=models.DO_NOTHING)

    def summary(self):
        return "Name: {} \nDescription: {} \nSection: {} \nCompany: {} \nExpiring: {} \n".format(self.name,
                                                                                                 self.description,
                                                                                                 self.section,
                                                                                                 self.company,
                                                                                                 self.expiry_date)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "Name: {} \n Description: {} \n Section: {} \n Company: {} \n Expiring: {} \n".format(self.name,
                                                                                                     self.description,
                                                                                                     self.section,
                                                                                                     self.company,
                                                                                                     self.expiry_date)


