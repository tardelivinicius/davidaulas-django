from rest_framework import serializers, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from roomclass.models import RoomClass


class RoomClassSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()

    def get_student(self, obj):
        student = {
            "id": obj.student.id,
            "name": obj.student.name
        }
        return student

    def get_course(self, obj):
        course = {
            "id": obj.course.id,
            "name": obj.course.name
        }
        return course

    class Meta:
        model = RoomClass
        fields = [
                  'id',
                  'student',
                  'course',
                  'date_joined',
                  'status',
                  'observation_class'
                 ]

    def create(self, validated_data):
        student = validated_data.pop('student', None)
        course = validated_data.pop('course', None)
        instance = RoomClass(student_id=student, course_id=course)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        student =
        instance.student = student
        course = validated_data.pop('course', None)
        instance.course = course
        instance.save()
        return instance

