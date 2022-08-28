from dataclasses import field
from rest_framework import serializers
from .models import Opay
from django.core.validators import URLValidator


class OpaySerializer(serializers.HyperlinkedModelSerializer):
    # Make twitchId ReadOnly (We Make this api need Auth so It can take from token
    twitchId = serializers.ReadOnlyField(source='twitchId.username')

    class Meta:
        model = Opay
        fields = ("opay_link", 'ecpay_link', 'twitchId')

    def validate_opay_link(self, value):
        cont = "https://payment.opay.tw/Broadcaster/AlertBox"
        if cont not in value:
            raise serializers.ValidationError("Not a opay Link")
        return super().validate(value)

    def validate_ecpay_link(self, attrs):
        cont = "https://payment.ecpay.com.tw/Broadcaster/AlertBox"
        if cont not in attrs:
            raise serializers.ValidationError("Not a ecpay Link")
        return super().validate(attrs)
