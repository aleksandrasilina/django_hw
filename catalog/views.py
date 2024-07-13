import json
from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from catalog.forms import UploadFileForm
from catalog.models import Product


def handle_uploaded_file(f):
    with open(f"media/catalog/photo/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def save_product_data(product_data):
    with open("new_product.json", "w", encoding="utf-8") as file:
        json.dump(product_data, file, ensure_ascii=False, indent=4)


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')

        form = UploadFileForm(request.POST, request.FILES)

        product_data = {
            'name': name,
            'description': description,
            'photo': f'catalog/photo/{request.FILES['file'].name}',
            'category': category,
            'price': price
        }
        save_product_data(product_data)

        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()

    # pprint(Product.objects.order_by("created_at")[1:6:-1])

    object_list = Product.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        "products": products,
        'page': page,
        'form': form,
        'title': 'Главная',
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
