from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from .models import Surah
from .serializers import SurahSerializer


class GetQuran(APITestCase):
    '''Checking Quran app API'''
    client = APIClient()

    def test_get_surahs(self):
        """
        This test ensures that surahs is loaded correctly to database
        making a GET request to the quran/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("surahs-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Surah.objects.all()
        serialized = SurahSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check number of Surahs
        self.assertEqual(len(response.data), 114)
