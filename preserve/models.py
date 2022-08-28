from importlib.metadata import requires
from turtle import back
from django.db import models

# Create your models here.
from django.conf import settings

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from userprofile.models import Profile


class Preserve(models.Model):


    streamer = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    preserve_time = models.DateField()
    game = models.CharField(max_length=100, blank=False, default='')
    who = models.CharField(max_length=100, blank=False)
    
    class Meta:
        ordering = ['created']
