from django.urls import path

from notifier.views import *

urlpatterns = [
    path('', get_notifs, name="notifications"),
    path('add', NotifsViewCreate.as_view(), name="notifs_create"),
    path('<int:pk>/update', NotifsViewUpdate.as_view(), name="notifs_update"),
    path('<int:pk>/delete', delete_notif, name="notifs_delete"),
    path('<int:pk>/acknowledge/<int:contract>/', acknowledge_contract, name="acknowledge"),
]
