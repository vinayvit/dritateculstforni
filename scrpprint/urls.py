# insta_project/urls.py
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from django.views.generic.base import TemplateView
from django.conf.urls import include, url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scrp.urls')),
]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
	
