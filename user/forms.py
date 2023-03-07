from django import forms
from .models import *

class EducationForm(forms.ModelForm):

    class Meta:
        model= Education
        fields=('service','quantity','phone_number')
        labels={}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].queryset = Checker.objects.none()

        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['quantity'].queryset = Checker.objects.filter(service_id=service_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['quantity'].queryset = self.instance.service.plan_set

class ElectForm(forms.ModelForm):

    class Meta:
        model= Elect
        fields=('service','phone_number','amount','meter_number','recharge_now','schedule_for_later','one_off','auto_renew')
        labels={}

class DataForm(forms.ModelForm):

    class Meta:
        model= Data
        fields=('service','plan','phone_number','recharge_now','schedule_for_later','one_off','auto_renew')
        labels={}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plan'].queryset = Plan.objects.none()

        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['plan'].queryset = Plan.objects.filter(service_id=service_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['plan'].queryset = self.instance.service.plan_set

class AirtimeForm(forms.ModelForm):

    class Meta:
        model= Airtime
        fields=('choose_network','phone_number','amount')
        labels={}

class BankForm(forms.ModelForm):

    class Meta:
        model= Bank
        fields=('bank_name','account_name','account_number')
        labels={}

class WithForm(forms.ModelForm):

    class Meta:
        model= With
        fields=('amount',)
        labels={}

class CableForm(forms.ModelForm):

    class Meta:
        model= Cable
        fields=('service','choose_type','plan','card_number','recharge_now','schedule_for_later','one_off','auto_renew')
        labels={}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['plan'].queryset = CablePlan.objects.none()

        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['plan'].queryset = CablePlan.objects.filter(service_id=service_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['plan'].queryset = self.instance.service.plan_set
