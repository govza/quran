from django.db import models


class Reciter(models.Model):
    '''General information about Reciter'''
    name = models.CharField(max_length=100)
    quality = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)


class Recitation(models.Model):
    '''General information about Recitation'''
    ayah = models.PositiveIntegerField()
    segments = models.TextField()
    surah = models.ForeignKey(
        'quran.Surah',
        on_delete=models.CASCADE,
        related_name='recitation')
    reciter = models.ForeignKey(
        Reciter,
        on_delete=models.CASCADE,
        related_name='recitation')

    class Meta:
        ordering = ['ayah']
