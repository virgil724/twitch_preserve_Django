from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from userprofile.models import Profile

from userprofile.serializers import ProfileSerializers
from rest_framework import permissions


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Profile.objects.filter(user=self.request.user)
        return queryset
