from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'email': TextInput(attrs={'class': 'form-control','placeholder':'Email'}),
            'message': Textarea(attrs={'class': 'form-control','placeholder':'Message'}),
        }