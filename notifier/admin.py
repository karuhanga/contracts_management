from django.contrib import admin

from .models import NotificationPoint, NotificationStatus

# Register your models here.
admin.site.register(NotificationPoint)
admin.site.register(NotificationStatus)
