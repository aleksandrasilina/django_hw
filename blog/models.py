from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок", help_text="Введите заголовок статьи")
    content = models.TextField(verbose_name="Содержимое", help_text="Введите содержимое")
    preview = models.ImageField(upload_to="blog/previews", verbose_name="Превью",
                                help_text="Загрузите изображение для превью", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания",
                                      help_text="Укажите дату создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано",
                                       help_text="Укажите, опубликована статья или нет")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров",
                                      help_text="Укажите количество просмотров")
    slug = models.CharField(max_length=150, verbose_name='Slug', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created_at']
