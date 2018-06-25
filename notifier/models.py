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
    class Meta:
        verbose_name_plural = "Notification Statuses"

    contract = models.ForeignKey('core.Contract', on_delete=models.CASCADE)
    notification_point = models.ForeignKey('NotificationPoint', on_delete=models.CASCADE)
    action_taken = models.BooleanField(default=False)

    def __str__(self):
        return self.contract.name + " at " + self.notification_point.name
