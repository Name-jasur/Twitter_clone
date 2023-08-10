from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('', include('dwitter.urls'), name='dwitter'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


