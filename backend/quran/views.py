from rest_framework import generics
from .models import Surah
from .serializers import SurahSerializer


class SurahListView(generics.ListAPIView):
    """
    Provides a get method handler for Surahs.
    """
    queryset = Surah.objects.all()
    serializer_class = SurahSerializer
