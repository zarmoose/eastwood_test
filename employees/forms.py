from django import forms
from . import models


class FilterForm(forms.Form):
    department = forms.ModelChoiceField(
        label='Отдел',
        queryset=models.Department.objects.all(),
        empty_label='Все',
        required=False
    )
    working = forms.BooleanField(label='Только работающие', required=False)
