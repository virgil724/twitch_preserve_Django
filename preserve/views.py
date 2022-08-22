from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins

from .serializers import PreserveSerializer,UserSerializer
from django.contrib.auth.models import User
from .models import Preserve

# Create your views here.


class PreserveViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):

    queryset = Preserve.objects.all()
    serializer_class = PreserveSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer