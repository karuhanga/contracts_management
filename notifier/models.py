from django.db import models


# Create your models here.
from django.urls import reverse


class NotificationPoint(models.Model):
    name = models.CharField(max_length=30)
    when_time_left = models.IntegerField()  # counted in days

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class NotificationStatus(models.Model):
    contract = models.ForeignKey('core.ContractManager', on_delete=models.CASCADE)
    action_taken = False
