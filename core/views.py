from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.forms import ContractForm, SectionForm, ContractManagerForm, CompanyForm

from core.models import Contract, Section, ContractManager, Company
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


class SectionViewCreate(CreateView):
    model = Section
    form_class = SectionForm


class SectionViewUpdate(UpdateView):
    model = Section
    form_class = SectionForm


class SectionViewDelete(DeleteView):
    model = Section
    success_url = SUCCESS_URL


class ContractManagerViewCreate(CreateView):
    model = ContractManager
    form_class = ContractManagerForm


class ContractManagerViewUpdate(UpdateView):
    model = ContractManager
    form_class = ContractManagerForm


class ContractManagerViewDelete(DeleteView):
    model = ContractManager
    success_url = SUCCESS_URL


class CompanyViewCreate(CreateView):
    model = Company
    form_class = CompanyForm


class CompanyViewUpdate(UpdateView):
    model = Company
    form_class = CompanyForm


class CompanyViewDelete(DeleteView):
    model = Company
    success_url = SUCCESS_URL


def success(request):
    return render(request, 'success.html')
