from rest_framework import serializers, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = [
                  'id',
                  'name',
                  'value',
                  'status'
                 ]

class CourseClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name',]