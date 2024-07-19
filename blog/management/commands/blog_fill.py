from django.core.management import BaseCommand

from blog.models import Author, Article
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_authors():
        authors = []
        with open("blog.json", "r", encoding="utf-8") as file:
            for author in json.load(file):
                if author["model"] == "blog.author":
                    authors.append(author["fields"])
        return authors

    @staticmethod
    def json_read_articles():
        articles = []
        with open("blog.json", "r", encoding="utf-8") as file:
            for article in json.load(file):
                if article["model"] == "blog.article":
                    articles.append(article["fields"])
        return articles

    def handle(self, *args, **options):

        Author.objects.all().delete()
        Article.objects.all().delete()
        Author.truncate_table_restart_id()

        authors_for_create = []
        articles_for_create = []

        for author in Command.json_read_authors():
            authors_for_create.append(Author(**author))

        Author.objects.bulk_create(authors_for_create)

        for article in Command.json_read_articles():
            article['author'] = Author.objects.get(pk=article["author"])
            articles_for_create.append(Article(**article))

        Article.objects.bulk_create(articles_for_create)
        dct = {"title": "Тест",
               "content": "Обезьяны лазят по лианам",
               "preview": "blog/previews/images.jpg",
               "created_at": "2024-07-17T20:23:33.707Z",
               "is_published": True,
               "views_count": 6,
               "slug": "ob-obezyanah",
               "author": Author.objects.get(pk=1)}
        Article.objects.create(**dct)

        print("Authors and articles created successfully!")
