import json
from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView

from catalog.forms import UploadFileForm
from catalog.models import Product


def handle_uploaded_file(f):
    with open(f"media/catalog/photo/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def save_product_data(product_data):
    with open("new_product.json", "w", encoding="utf-8") as file:
        json.dump(product_data, file, ensure_ascii=False, indent=4)


class ProductListView(ListView):
    model = Product
    paginate_by = 3
    extra_context = {
        'title': 'Главная'
    }


class ProductDetailView(DetailView):
    model = Product



def contacts(request):
    context = {
        'title': 'Контакты'
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        with open('messages.txt', 'a') as file:
            file.write(f'{name}({email}): {message}\n')

    # contacts_data = {}
    # with open('contacts.json', 'r', encoding='utf-8') as file:
    #     for i, contact in enumerate(json.load(file), 1):
    #         contacts_data[str(i)] = contact['fields']

    return render(request, 'contacts.html', context)



