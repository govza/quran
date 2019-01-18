from rest_framework import serializers

from .models import Recitation, Reciter


class ReciterSerializer(serializers.ModelSerializer):
    '''Serializer for Reciter model'''
    class Meta:
        model = Reciter
        fields = '__all__'


class RecitationSerializer(serializers.ModelSerializer):
    '''Serializer for Recitation model'''

    class Meta:
        model = Recitation
        fields = ('ayah', 'segments')
