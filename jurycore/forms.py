from colorful.forms import RGBColorField
from django import forms

from .models import Delegate, Booklet, Committee, Delegation


class DelegateForm(forms.ModelForm):
    """ Form for creating a delegate """

    class Meta:
        model = Delegate
        fields = [
            'name',
            'photo',
            'committee',
            'delegation',
            'remarks'
        ]




class BookletForm(forms.ModelForm):
    """ Form for creating a booklet """

    class Meta:
        model = Booklet
        fields = [
            'session_name',
        ]


class CommitteeForm(forms.ModelForm):
    """ Form for creating a committee """

    class Meta:
        model = Committee
        fields = [
            'name',
        ]


class DelegationForm(forms.ModelForm):
    """ Form for creating a delegation """

    colour = RGBColorField(help_text='Optional, defaults to black. Choose dark colours.')

    class Meta:
        model = Delegation
        fields = [
            'name',
            'colour',
        ]
