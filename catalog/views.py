from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView

from catalog.forms import ContactUsForm, ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product
    paginate_by = 3
    extra_context = {
        'title': 'Главная'
    }

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        for product in context_data.get('object_list'):
            product.version = product.version_set.filter(is_active=True).first()
        return context_data


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['product'].name
        self.object.version = self.object.version_set.filter(is_active=True).first()
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        if self.object.version_set.filter(is_active=True).count() > 1:
            form.add_error(None, 'Активной может быть только одна версия')
            return self.form_invalid(form)
        return super().form_valid(form)


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactUsForm()
        return context

    @staticmethod
    def post(request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
            with open('messages.txt', 'a') as file:
                file.write(f'{name}({email}): {message}\n')
        else:
            ContactUsForm()

        return render(request, 'catalog/contacts.html', {'form': form})
