from django import forms
from core.models import ContractManager,Section,Company,Contract

#Here are forms for input

class ContractManagerForm(forms.ModelForm):

    class Meta:
        model = ContractManager
        fields = ('name','email','contract')






class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ('name','description')

        class ContractManagerForm(forms.ModelForm):
            class Meta:
                model = ContractManager
                fields = ('name', 'email', 'contract')


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name','contract_person','email','contract' )


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ('name','description','section','company','start_date','expiry_date','contract_manager' )


