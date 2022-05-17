from django import forms
from .models import Vacation


class VacationForm(forms.ModelForm):

    class Meta:
        model = Vacation
        fields = ('start_date','end_date')