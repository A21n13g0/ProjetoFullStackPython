from django.forms import ModelForm
from django import forms
from app.models import Supplier

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier', 'cnpj', 'stateRegistration', 'telephone', 'email']