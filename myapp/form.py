from django import forms
from .models import *

class Employeeform(forms.ModelForm):
    class Meta:
        form=Employee
        fields='__all__'
