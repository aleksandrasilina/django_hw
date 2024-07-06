from django.core.management import BaseCommand

from catalog.models import Product, Category
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        categories = []
        with open("catalog.json", "r", encoding="utf-8") as file:
            for category in json.load(file):
                if category["model"] == "catalog.category":
                    categories.append(category["fields"])
        return categories

    @staticmethod
    def json_read_products():
        products = []
        with open("catalog.json", "r", encoding="utf-8") as file:
            for product in json.load(file):
                if product["model"] == "catalog.product":
                    products.append(product["fields"])
        return products

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()
        Category.truncate_table_restart_id()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product["name"],
                    description=product["description"],
                    photo=product["photo"],
                    category=Category.objects.get(pk=product["category"]),
                    price=product["price"],
                    created_at=product["created_at"],
                    updated_at=product["updated_at"],
                )
            )

        Product.objects.bulk_create(product_for_create)
