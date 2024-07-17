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


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'photo', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')


# def contacts(request):
#     context = {
#         'title': 'Контакты'
#     }
#
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         with open('messages.txt', 'a') as file:
#             file.write(f'{name}({email}): {message}\n')
#
#     return render(request, 'contacts.html', context)

class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request):
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

