from rest_framework import serializers
from .models import Surah


class SurahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surah
        fields = '__all__'
