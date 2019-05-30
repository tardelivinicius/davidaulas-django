from rest_framework import serializers, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from roomclass.models import RoomClass
from student.serializers import StudentClassSerializer
from courses.serializers import CourseClassSerializer

class RoomClassSerializer(serializers.ModelSerializer):
    student = StudentClassSerializer(many=False)
    course = CourseClassSerializer(many=False)

    class Meta:
        model = RoomClass
        fields = ['id',
                  'student',
                  'course',
                  'date',
                  'status'
                 ]

        
