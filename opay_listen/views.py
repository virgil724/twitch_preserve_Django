from django.shortcuts import render

# Create your views here.
from .models import Opay
from .serializers import OpaySerializer
from rest_framework import viewsets
from rest_framework import mixins

from rest_framework import permissions


class OpayView(viewsets.ModelViewSet):
    queryset = Opay.objects.all()
    serializer_class = OpaySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(twitchId=self.request.user)
