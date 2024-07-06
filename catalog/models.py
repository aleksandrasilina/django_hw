from django.db import models, connection
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории", **NULLABLE
    )

    def __str__(self):
        return self.name

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Продукт", help_text="Введите название продукта"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта", **NULLABLE
    )
    photo = models.ImageField(
        upload_to="catalog/photo",
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
        **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        related_name="products"
    )
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена", help_text="Введите цену продукта")
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания",
        help_text="Введите дату создания продукта",
    )
    updated_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата изменения",
        help_text="Введите дату последнего изменения продукта",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя контакта", help_text="Введите имя контакта")
    email = models.EmailField(verbose_name="Email", help_text="Введите email")
    message = models.TextField(verbose_name="Сообщение", help_text="Введите сообщение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ("name",)
