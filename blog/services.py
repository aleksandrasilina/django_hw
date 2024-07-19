from django.conf import settings
from django.core.mail import send_mail


def send_order_email(article_object):
    send_mail(
        'Поздравляем',
        f'Дорогой {article_object.author.name}, ваша статья {article_object.title} достигла 100 просмотров!',
        settings.EMAIL_HOST_USER,
        [article_object.author.email, 'al.a.silina@yandex.ru']
    )
