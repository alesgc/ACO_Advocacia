from django import forms
from .models import ContactPerson


class FormContact(forms.ModelForm):
    class Meta:
        model = ContactPerson
        fields = [
            'name',
            'phone',
            'email',
            'subject',
            'topic'
        ]
