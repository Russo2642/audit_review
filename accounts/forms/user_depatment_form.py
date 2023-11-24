from django import forms
from accounts.models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', )
        labels = {'name': 'Название департамента'}
