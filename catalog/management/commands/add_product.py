from django.core.management import BaseCommand

from catalog.models import Product, Category
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_new_product():
        with open("new_product.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def handle(self, *args, **options):
        product = Command.json_read_new_product()
        product['category'] = Category.objects.get(pk=product["category"])
        Product.objects.create(**product)
