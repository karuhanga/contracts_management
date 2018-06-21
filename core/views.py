from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.forms import ContractForm
from core.models import Contract
from core.utils.StringUtils import SUCCESS_URL


class ContractsViewCreate(CreateView):
    model = Contract
    form_class = ContractForm


class ContractsViewUpdate(UpdateView):
    model = Contract
    form_class = ContractForm


class ContractsViewDelete(DeleteView):
    model = Contract
    success_url = SUCCESS_URL


def success(request):
    return render(request, 'success.html')
