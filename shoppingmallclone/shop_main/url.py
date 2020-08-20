from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop_main'

urlpatterns = [
    url(r'^$', views.Shop_main.as_view(), name='shop_main'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)