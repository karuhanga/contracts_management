"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from core import views
from core.views import ContractsViewCreate, ContractsViewUpdate, ContractsViewRetrieve, \
    ContractManagerViewRetrieve, SectionsViewRetrieve, CompanyViewRetrieve, delete_contract
from core.views import CompanyViewCreate, delete_company, CompanyViewUpdate
from core.views import ContractManagerViewCreate, ContractManagerViewUpdate, delete_manager


urlpatterns = [
    path('', views.home, name="dashboard"),
    path('success', views.success, name="success"),
    path('contracts', views.get_contracts, name="contracts_retrieve"),
    path('contracts_sec', views.get_contracts_sec, name="contracts_sec_retrieve"),
    path('contracts/add', ContractsViewCreate.as_view(), name="contracts_create"),
    path('contracts/<int:pk>', ContractsViewRetrieve.as_view(), name="contract"),
    path('contracts/<int:pk>/update', ContractsViewUpdate.as_view(), name="contracts_update"),
    path('contracts/<int:pk>/delete', delete_contract, name="contracts_delete"),

    path('managers', views.get_managers, name="managers_retrieve"),
    path('managers/add', ContractManagerViewCreate.as_view(), name="managers_create"),
    path('managers/<int:pk>', ContractManagerViewRetrieve.as_view(), name="manager"),
    path('managers/<int:pk>/update', ContractManagerViewUpdate.as_view(), name="managers_update"),
    path('managers/<int:pk>/delete', delete_manager, name="managers_delete"),

    path('sections', views.get_sections, name="sections_retrieve"),
    path('sections/<int:pk>', SectionsViewRetrieve.as_view(), name="section"),

    path('companies', views.get_companies, name="companies_retrieve"),
    path('companies/add', CompanyViewCreate.as_view(), name="companies_create"),
    path('companies/<int:pk>', CompanyViewRetrieve.as_view(), name="company"),
    path('companies/<int:pk>/update', CompanyViewUpdate.as_view(), name="companies_update"),
    path('companies/<int:pk>/delete', delete_company, name="companies_delete")
]
