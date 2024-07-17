from django import forms

from catalog.models import Contact


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)
