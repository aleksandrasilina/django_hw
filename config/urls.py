from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('catalog.urls', namespace='catalog')),
                  path('blog/', include('blog.urls', namespace='blog'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()
