import json
from pprint import pprint

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from catalog.models import Product


def home(request):
    # pprint(Product.objects.order_by("created_at")[1:6:-1])
    object_list = Product.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        "products": products,
        'page': page,
        'title': 'Главная'
    }
    return render(request, 'home.html', context)


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


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
        'title': Product.objects.get(pk=pk)
    }
    return render(request, 'product_detail.html', context)
