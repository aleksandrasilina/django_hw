from django import forms

from catalog.models import Contact, Product

FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар'
]


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError('Имя продукта содержит запрещенное слово')
        return name


    def clean_description(self):
        description = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError('Описание продукта содержит запрещенное слово')
        return description
