import json
from pprint import pprint

from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    pprint(Product.objects.order_by("created_at")[1:6:-1])
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        with open('messages.txt', 'a') as file:
            file.write(f'{name}({email}): {message}\n')

    contacts_data = {}
    with open('contacts.json', 'r', encoding='utf-8') as file:
        for i, contact in enumerate(json.load(file), 1):
            contacts_data[str(i)] = contact['fields']

    return render(request, 'contacts.html', context=contacts_data)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)
