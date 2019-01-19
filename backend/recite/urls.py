'''Recite app api url endpoints'''
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(
        r'recite/(?P<reciter_id>\d+)/(?P<surah_id>\d+)/$',
        views.RecitationListView.as_view(),
        name="reciter-recitations"
    ),
    re_path(
        r'recite/(?P<reciter_id>\d+)/$',
        views.ReciterDetailsView.as_view(),
        name="reciter-details",
    ),
    re_path(
        r'recite/$',
        views.ReciterListView.as_view(),
        name="reciters-all",
    )
]
