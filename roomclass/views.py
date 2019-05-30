from rest_framework import viewsets, status
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from roomclass.models import RoomClass
from roomclass.serializers import RoomClassSerializer
from django.shortcuts import get_object_or_404



class RoomClassViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = RoomClassSerializer

    def get_queryset(self):
        return RoomClass.objects.all()
