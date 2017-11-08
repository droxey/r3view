from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.dashboard.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
