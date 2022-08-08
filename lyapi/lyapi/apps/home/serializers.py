from .models import Nav
from rest_framework import serializers


class NavModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = ['id', 'title', 'link', 'position']
