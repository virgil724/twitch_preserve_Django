from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from .serializers import PreserveSerializer
from .models import Preserve
from django.utils.encoding import force_str
from userprofile.models import Profile
# Create your views here.
from django.contrib.auth import get_user_model

from rest_framework.metadata import SimpleMetadata

# https://github.com/encode/django-rest-framework/issues/3751#issuecomment-287640261
class CustomMetadata(SimpleMetadata):

    def get_field_info(self, field):
        field_info = super().get_field_info(field)
       
        if (not field_info.get('read_only') and
                hasattr(field, 'choices')):
            
            field_info['choices'] = [
                {
                    'value': choice_value,
                    'display_name': Profile.objects.get(user=get_user_model().objects.get(id=choice_value)).nameCN
                }
                for choice_value, choice_name in field.choices.items()
            ]

        return field_info


class PreserveViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):

    queryset = Preserve.objects.all()
    serializer_class = PreserveSerializer
    metadata_class = CustomMetadata
