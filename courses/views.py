from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from courses.models import Course
from courses.serializers import CourseSerializer
from django.shortcuts import get_object_or_404


class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        queryset = queryset.prefetch_related(
            'date_course'
        )
        return queryset
    
    def destroy(self, request, pk=None):
        course = get_object_or_404(Course.objects.filter(pk=pk))
        course.status = 3
        course.save()

        return Response({"detail:" "success"}, status=status.HTTP_200_OK)