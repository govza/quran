from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import status

from . import serializers
from .models import Recitation, Reciter


class ReciterListView(generics.ListAPIView):
    '''
    Provides a get method handler for list of Reciters.
    '''
    queryset = Reciter.objects.all()
    serializer_class = serializers.ReciterSerializer


class RecitationListView(generics.ListAPIView):
    '''
    Provides a get method handler for list of Surah Recitations.
    '''
    serializer_class = serializers.RecitationSerializer

    def get_queryset(self):
        reciter = self.kwargs['reciter_id']
        surah = self.kwargs['surah_id']

        recitations = Recitation.objects.filter(surah=surah, reciter=reciter)

        if recitations:
            return recitations

        raise NotFound()


class ReciterDetailsView(generics.RetrieveAPIView):
    '''
    Provides a get method handler for Reciter information
    '''
    queryset = Reciter.objects.all()
    serializer_class = serializers.ReciterSerializer

    def get(self, request, *args, **kwargs):
        try:
            reciter = self.queryset.get(id=kwargs["reciter_id"])
            return Response(serializers.ReciterSerializer(reciter).data)
        except Reciter.DoesNotExist:
            return Response(
                data={
                    "message": "Reciter with id: {} does not exist".format(
                        kwargs["reciter_id"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
