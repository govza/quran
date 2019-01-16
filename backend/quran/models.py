'''Models of Quran app'''
from django.db import models


class Surah(models.Model):
    '''Information about Surahs'''
    number = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    total_ayahs = models.PositiveIntegerField()


class Ayah(models.Model):
    '''Information about Ayah'''
    number = models.PositiveIntegerField()
    text = models.TextField()
    surah = models.ForeignKey(
        Surah,
        on_delete=models.CASCADE,
        related_name='ayahs')

    class Meta:
        ordering = ['number']
