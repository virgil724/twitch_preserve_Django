from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from .serializers import UserSerializer
from django.contrib.auth import get_user_model
# Create your views here.


class AccountView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


