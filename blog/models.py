from django.db import models, connection

NULLABLE = {"blank": True, "null": True}


class Author(models.Model):
    name = models.CharField(max_length=150, verbose_name="Автор", help_text="Введите имя автора", **NULLABLE)
    email = models.EmailField(verbose_name='Почта')

    def __str__(self):
        return f'{self.name}({self.email})'

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Article(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Заголовок", help_text="Введите заголовок статьи"
    )
    content = models.TextField(
        verbose_name="Содержимое", help_text="Введите содержимое"
    )
    preview = models.ImageField(
        upload_to="blog/previews",
        verbose_name="Превью",
        help_text="Загрузите изображение для превью",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Укажите, опубликована статья или нет",
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
    )
    slug = models.CharField(max_length=150, verbose_name="Slug", **NULLABLE)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, verbose_name="Автор", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]
