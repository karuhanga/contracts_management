from django import forms
from core.models import ContractManager,Section,Company,Contract


# Here are forms for input


class ContractManagerForm(forms.ModelForm):
    class Meta:
        model = ContractManager
        fields = '__all__'


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
