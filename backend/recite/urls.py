'''Recite app api url endpoints'''
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        r'api/(?P<version>(v1|v2))/recite/(?P<reciter>\d+)/(?P<surah>\d+)/$',
        views.RecitationListView.as_view(),
        name="reciter-recitations"
    ),
    re_path(
        r'api/(?P<version>(v1|v2))/recite/(?P<reciter>\d+)/$',
        views.ReciterDetailsView.as_view(),
        name="reciter-details",
    ),
    re_path(
        r'api/(?P<version>(v1|v2))/recite/$',
        views.ReciterListView.as_view(),
        name="reciters-all",
    )
]
