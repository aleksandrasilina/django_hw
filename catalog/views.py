from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView

from catalog.forms import ContactUsForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 3
    extra_context = {
        'title': 'Главная'
    }


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['product'].name
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'photo', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')


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
