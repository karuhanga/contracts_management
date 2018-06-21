from django import forms
from core.models import ContractManager,Section,Company,Contract


# Here are forms for input
from core.utils.StringUtils import CLASS, INPUT, TEXT_AREA, SELECT


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

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({CLASS: INPUT})
        self.fields['description'].widget.attrs.update({CLASS: TEXT_AREA, 'rows': '3'})
        self.fields['section'].widget.attrs.update({CLASS: SELECT})
        self.fields['company'].widget.attrs.update({CLASS: SELECT})
        self.fields['start_date'].widget.attrs.update({CLASS: INPUT})
        self.fields['expiry_date'].widget.attrs.update({CLASS: INPUT})
        self.fields['contract_manager'].widget.attrs.update({INPUT: SELECT})
