from rest_framework import viewsets, status
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from roomclass.models import RoomClass
from roomclass.serializers import RoomClassSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from student.models import Student

class RoomClassViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = RoomClassSerializer

    def get_queryset(self):
        return RoomClass.objects.all().exclude(status=3).distinct().order_by('date_joined')

        return queryset

    def create(self, request):
        serializer = self.get_serializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(student=request.data.pop('student', None), course=request.data.pop('course', None))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, request, pk=None):
        course = get_object_or_404(self.get_queryset().filter(pk=pk))
        serializer = self.get_serializer(course, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(student=request.data.pop('student', None), course=request.data.pop('course', None))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

