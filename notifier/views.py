import json

from django.core import serializers
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from core.models import Contract
from core.utils.StringUtils import SUCCESS_URL
from notifier.forms import NotificationPointForm
from notifier.models import NotificationPoint, NotificationStatus


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


def delete_notif(request, pk=None):
    if pk is None:
        return HttpResponseBadRequest()

    try:
        item = NotificationPoint.objects.get(pk=pk)
        item.delete()
        return redirect(SUCCESS_URL)
    except Exception:
        return HttpResponseServerError()


def acknowledge_contract(request, pk=None, contract=None):
    if (not pk) or (not contract):
        return HttpResponseServerError()

    contract = Contract.objects.get(pk=contract)
    notification_point = NotificationPoint.objects.get(pk=pk)
    status, created = NotificationStatus.objects.get_or_create(contract=contract, notification_point=notification_point)
    status.action_taken = True
    status.save()
    return redirect(contract.get_absolute_url())
