from dataclasses import field
from rest_framework import serializers
from .models import Preserve
from django.contrib.auth.models import User


class PreserveSerializer(serializers.HyperlinkedModelSerializer):
    created=serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta():
        model = Preserve
        fields = ['id','created','preserve_time',
                  'game',
                  'who',
                  'streamer']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    preserve = serializers.HyperlinkedRelatedField(
        many=True, view_name='preserve-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'preserve']
