Онлайн_магазин овощей и фруктов
Блог о природе

Для подключения к базе данных введите пароль в поле PASSWORD в config/settings.py

Наполнение каталога продуктами: python manage.py fill
Наполнение блога статьями: python manage.py blog_fill

Для отправки email введите свои почту и пароль в полях EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
в config/settings.py. Также в функции send_order_email в blog/services.py измените 
атрибут recipient_list


