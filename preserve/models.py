from importlib.metadata import requires
from turtle import back
from django.db import models

# Create your models here.
from django.conf import settings

from django.utils.translation import gettext_lazy as _

class Preserve(models.Model):
    class Streamer(models.TextChoices):
        MAPLESYRUP = 'maplesyrup_0726',_('楓糖兒__')

    streamer = models.TextField(choices=Streamer.choices)

    created = models.DateTimeField(auto_now_add=True)
    preserve_time = models.DateField()
    game = models.CharField(max_length=100, blank=False, default='')
    who = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['created']

