from django import forms
from django.forms import BooleanField

from catalog.models import Contact, Product

FORBIDDEN_WORDS = (
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар'
)


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ContactUsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductForm(forms.ModelForm):
    error_css_class = "is-invalid"

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word in name.lower():
                raise forms.ValidationError('Имя продукта содержит запрещенное слово')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError('Описание продукта содержит запрещенное слово')
        return description


class VersionForm(forms.ModelForm):
    error_css_class = "is-invalid"

    class Meta:
        model = Product
        exclude = '__all__'
