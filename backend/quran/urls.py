from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        'api/(?P<version>(v1|v2))/quran',
        views.SurahListView.as_view(),
        name="surahs-all",
    ),
]