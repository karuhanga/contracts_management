from django.core import serializers
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect

import json

# Create your views here.
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.forms import ContractForm, SectionForm, ContractManagerForm, CompanyForm

from core.models import Contract, Section, ContractManager, Company
from core.utils.StringUtils import SUCCESS_URL


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


def home(request):
    return render(request, "dashboard.html")


def get_contracts(request):
    data = jsonify(Contract.objects.order_by('expiry_date').all())
    for datum in data:
        datum["section"] = Section.objects.get(pk=datum["section"]).name
        datum["company"] = Company.objects.get(pk=datum["company"]).name
        datum["contract_manager"] = ContractManager.objects.get(pk=datum["contract_manager"]).name
    return JsonResponse(data, safe=False)


def get_contracts_sec(request):
    data = jsonify(Contract.objects.order_by('section').all())
    for datum in data:
        datum["section"] = Section.objects.get(pk=datum["section"]).name
        datum["company"] = Company.objects.get(pk=datum["company"]).name
        datum["contract_manager"] = ContractManager.objects.get(pk=datum["contract_manager"]).name
    return JsonResponse(data, safe=False)


def get_companies(request):
    data = jsonify(Company.objects.all())
    return JsonResponse(data, safe=False)


def get_managers(request):
    data = jsonify(ContractManager.objects.all())
    return JsonResponse(data, safe=False)


def get_sections(request):
    data = jsonify(Section.objects.all())
    return JsonResponse(data, safe=False)


class ContractsViewRetrieve(DetailView):
    model = Contract


class ContractsViewCreate(CreateView):
    model = Contract
    form_class = ContractForm


class ContractsViewUpdate(UpdateView):
    model = Contract
    form_class = ContractForm


def delete_contract(request, pk=None):
    if pk is None:
        return HttpResponseBadRequest()

    try:
        item = Contract.objects.get(pk=pk)
        item.delete()
        return redirect(SUCCESS_URL)
    except Exception:
        return HttpResponseServerError()


class SectionsViewRetrieve(DetailView):
    model = Section


class SectionViewCreate(CreateView):
    model = Section
    form_class = SectionForm


class SectionViewUpdate(UpdateView):
    model = Section
    form_class = SectionForm


def delete_manager(request, pk=None):
    if pk is None:
        return HttpResponseBadRequest()

    try:
        item = ContractManager.objects.get(pk=pk)
        item.delete()
        return redirect(SUCCESS_URL)
    except Exception as e:
        print(e)
        return HttpResponseServerError()


class ContractManagerViewRetrieve(DetailView):
    model = ContractManager


class ContractManagerViewCreate(CreateView):
    model = ContractManager
    form_class = ContractManagerForm


class ContractManagerViewUpdate(UpdateView):
    model = ContractManager
    form_class = ContractManagerForm


def delete_contract(request, pk=None):
    if pk is None:
        return HttpResponseBadRequest()

    try:
        item = Contract.objects.get(pk=pk)
        item.delete()
        return redirect(SUCCESS_URL)
    except Exception:
        return HttpResponseServerError()


class CompanyViewRetrieve(DetailView):
    model = Company


class CompanyViewCreate(CreateView):
    model = Company
    form_class = CompanyForm


class CompanyViewUpdate(UpdateView):
    model = Company
    form_class = CompanyForm


def delete_company(request, pk=None):
    if pk is None:
        return HttpResponseBadRequest()

    try:
        item = Company.objects.get(pk=pk)
        item.delete()
        return redirect(SUCCESS_URL)
    except Exception:
        return HttpResponseServerError()


def success(request):
    return render(request, 'success.html')
