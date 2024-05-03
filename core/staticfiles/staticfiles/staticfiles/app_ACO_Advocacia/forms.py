from django import forms
from app_ACO_Advocacia.models import ContactPerson

class FormContact(forms.ModelForm):
    
    class Meta:
        model = ContactPerson
        fields = '__all__'