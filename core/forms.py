from django import forms
from core.models import ContractManager, Section, Company, Contract

from core.utils.StringUtils import CLASS, INPUT, TEXT_AREA, SELECT, CHECKBOX


class ContractManagerForm(forms.ModelForm):
    class Meta:
        model = ContractManager
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContractManagerForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({CLASS: INPUT})
        self.fields['email'].widget.attrs.update({CLASS: INPUT})
        self.fields['contact'].widget.attrs.update({CLASS: INPUT})


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({CLASS: INPUT})
        self.fields['description'].widget.attrs.update({CLASS: INPUT})
        self.fields['section_manager'].widget.attrs.update({CLASS: INPUT})
        self.fields['section_manager_email'].widget.attrs.update({CLASS: INPUT})


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({CLASS: INPUT})
        self.fields['contact_person'].widget.attrs.update({CLASS: INPUT})
        self.fields['email'].widget.attrs.update({CLASS: INPUT})
        self.fields['contact'].widget.attrs.update({CLASS: INPUT})


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
        self.fields['is_active'].widget.attrs.update({INPUT: CHECKBOX})
        self.fields['comments'].widget.attrs.update({CLASS: TEXT_AREA, 'rows': '3'})
