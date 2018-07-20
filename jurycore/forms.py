from django import forms

from .models import Delegate


class DelegateForm(forms.ModelForm):
    """Form for creating a delegate"""

    class Meta:
        model = Delegate
        fields = [
            'name',
            'photo',
            'committee',
            'delegation',
            'remarks'
        ]
