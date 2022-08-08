from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from .serializers import NavModelSerializers
from .models import Nav
from lyapi.settings import contains


class NavViews(ListAPIView):
    serializer_class = NavModelSerializers
    queryset = Nav.objects.filter(is_deleted=False, is_show=True, position=1)[0:contains.NAV_TOP_LENGTH]
