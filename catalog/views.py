import json
from pprint import pprint

from django.shortcuts import render


def home(request):
    with open("catalog.json", "r", encoding="utf-8") as file:
        products = [product["fields"] for product in json.load(file) if product["model"] == "catalog.product"]
        last_5_products = sorted(products, key=lambda x: x["created_at"], reverse=True)[:5]
        pprint(last_5_products)
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        with open('messages.txt', 'a') as file:
            file.write(f'{name}({email}): {message}\n')
    return render(request, 'contacts.html')
