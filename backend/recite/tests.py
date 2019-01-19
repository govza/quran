from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from .models import Reciter, Recitation
from .serializers import ReciterSerializer, RecitationSerializer


class GetRecite(APITestCase):
    '''Checking Recite app API'''
    client = APIClient()

    def test_get_reciters(self):
        '''
        This test ensures that reciters are loaded correctly to database
        making a GET request to the recite/ endpoint
        '''
        # hit the API endpoint
        response = self.client.get(
            reverse("reciters-all")
        )
        # fetch the data from db
        expected = Reciter.objects.all()
        serialized = ReciterSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reciter_details(self):
        '''
        This test ensures that reciters are loaded correctly to database
        making a GET request to the recite/{reciter_id} endpoint
        '''
        # hit the API endpoint for each surah
        reciters = Reciter.objects.all()

        for reciter in reciters:
            response = self.client.get(
                reverse(
                    "reciter-details",
                    kwargs={
                        "reciter_id": reciter.id
                    }
                )
            )
            # fetch the data from db
            expected = Reciter.objects.get(id=reciter.id)
            serialized = ReciterSerializer(expected)

            self.assertEqual(response.data, serialized.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_recitation_list(self):
        '''
        This test ensures that all reciter's recitations are loaded
        correctly to database making a GET request
        to the recite/{reciter_id}/{surah_id} endpoint
        '''
        # hit the API endpoint for each surah
        reciters = Reciter.objects.all()
        surahs = list(range(1, 115))

        for surah in surahs:
            for reciter in reciters:
                response = self.client.get(
                    reverse(
                        "reciter-recitations",
                        kwargs={
                            "reciter_id": reciter.id,
                            "surah_id": surah
                        }
                    )
                )
                # fetch the data from db
                expected = Recitation.objects.filter(
                    reciter=reciter.id, surah=surah)
                serialized = RecitationSerializer(expected, many=True)

                self.assertEqual(response.data, serialized.data)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
