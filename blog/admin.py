from django.contrib import admin

from blog.models import Article, Author


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_filter = ('author', 'is_published')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)
    list_filter = ('name', 'email',)
