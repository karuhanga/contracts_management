from django.db import models


# Create your models here.
class NotificationPoint(models.Model):
    name = models.CharField(max_length=30)
    when_time_left = models.IntegerField()  # counted in days


class NotificationStatus(models.Model):
    contract = models.ForeignKey('core.ContractManager', on_delete=models.CASCADE)
    action_taken = False
