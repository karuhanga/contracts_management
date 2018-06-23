import json

from django.core import serializers
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from core.utils.StringUtils import SUCCESS_URL
from notifier.forms import NotificationPointForm
from notifier.models import NotificationPoint


def jsonify(data):
    state_additions = {
        "popup_active": False
    }
    data = serializers.serialize('json', data)
    data = json.loads(data)
    for datum in data:
        fields = dict(datum["fields"])
        datum.update(fields)
        datum.update(state_additions)
        datum["fields"] = ""
    return data


def get_notifs(request):
    data = jsonify(NotificationPoint.objects.all())
    return JsonResponse(data, safe=False)


class NotifsViewCreate(CreateView):
    model = NotificationPoint
    form_class = NotificationPointForm
    success_url = SUCCESS_URL


class NotifsViewUpdate(UpdateView):
    model = NotificationPoint
    form_class = NotificationPointForm
    success_url = SUCCESS_URL


class NotifsViewDelete(DeleteView):
    model = NotificationPoint
    success_url = SUCCESS_URL
