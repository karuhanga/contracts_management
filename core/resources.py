from import_export import resources

from core.models import *


class SectionResource(resources.ModelResource):
    class Meta:
        model = Section


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company


class ContractResource(resources.ModelResource):
    class Meta:
        model = Contract


class ContractManagerResource(resources.ModelResource):
    class Meta:
        model = ContractManager
