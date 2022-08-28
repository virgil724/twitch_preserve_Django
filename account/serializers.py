
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    opay=serializers.HyperlinkedRelatedField(read_only=True,view_name="opay-detail")
    profile=serializers.HyperlinkedRelatedField(view_name="profile-detail",read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('url','username', 'password','opay','profile')

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
