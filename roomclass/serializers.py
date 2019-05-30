from rest_framework import serializers, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from roomclass.models import RoomClass


class RoomClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomClass
        fields = '__all__'
