from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from core.resources import *
from .models import Contract, Section, ContractManager, Company


admin.site.site_header = "Contracts Management"


class SectionAdmin(ImportExportModelAdmin):
    resource_class = SectionResource


class CompanyAdmin(ImportExportModelAdmin):
    resource_class = CompanyResource


class ContractAdmin(ImportExportModelAdmin):
    resource_class = ContractResource


class ContractManagerAdmin(ImportExportModelAdmin):
    resource_class = ContractManagerResource


# Register your models here.
admin.site.register(Contract, ContractAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(ContractManager, ContractManagerAdmin)
