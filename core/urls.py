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
from core.views import ContractsViewCreate, ContractsViewUpdate, ContractsViewDelete
from core.views import SectionViewCreate, SectionViewDelete, SectionViewUpdate
from core.views import CompanyViewCreate, CompanyViewDelete, CompanyViewUpdate
from core.views import ContractManagerViewCreate, ContractManagerViewUpdate, ContractManagerViewDelete




urlpatterns = [
    path('success', views.success, name="success"),
    path('contracts/add', ContractsViewCreate.as_view(), name="contracts_create"),
    path('contracts/<int:pk>/update', ContractsViewUpdate.as_view(), name="contracts_update"),
    path('contracts/<int:pk>/delete', ContractsViewDelete.as_view(), name="contracts_delete"),

    path('managers/add', ContractManagerViewCreate.as_view(), name="managers_create"),
    path('managers/<int:pk>/update', ContractManagerViewUpdate.as_view(), name="managers_update"),
    path('managers/<int:pk>/delete', ContractManagerViewDelete.as_view(), name="managers_delete"),

    path('sections/add', SectionViewCreate.as_view(), name="sections_create"),
    path('sections/<int:pk>/update', SectionViewUpdate.as_view(), name="sections_update"),
    path('sections/<int:pk>/delete', SectionViewDelete.as_view(), name="sections_delete"),

    path('companies/add', CompanyViewCreate.as_view(), name="companies_create"),
    path('companies/<int:pk>/update', CompanyViewUpdate.as_view(), name="companies_update"),
    path('companies/<int:pk>/delete', CompanyViewDelete.as_view(), name="companies_delete")



]
