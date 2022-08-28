from dataclasses import field
from rest_framework import serializers

from .models import Preserve
from django.contrib.auth import get_user_model


class PreserveSerializer(serializers.HyperlinkedModelSerializer):
    created = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    streamer = serializers.PrimaryKeyRelatedField(many=False
                                                   , queryset=get_user_model().objects.all())
    class Meta():

        model = Preserve
        fields = ['id', 'created', 'preserve_time',
                  'game',
                  'who',
                  'streamer']


