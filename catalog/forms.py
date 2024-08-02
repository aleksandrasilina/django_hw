from django import forms

from catalog.models import Contact, Product


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)
