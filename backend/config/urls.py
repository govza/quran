"""Project URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls(title='Quran API')),
    path('schema/', get_schema_view(title="Quran API")),
    path('admin/', admin.site.urls),
    path('', include('quran.urls')),
    path('', include('recite.urls')),
]
