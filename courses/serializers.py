from rest_framework import serializers, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from courses.models import Course, CourseDate


class CourseDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDate
        fields = ['id',
                  'day',
                  'hour'
                 ]

            
class CourseSerializer(serializers.ModelSerializer):
    date_course = CourseDateSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id',
                  'name',
                  'value',
                  'date_course',
                  'status'
                 ]

    def create(self, validated_data):

        dates = validated_data.pop('date_course')
        course = Course.objects.create(**validated_data)

        course.date_course.set(dates)

        return course

    
    def update(self, instance, validated_data):

        dates = validated_data.pop('date_course')

        instance.name = validated_data.get('name', instance.name)
        instance.value = validated_data.get('value', instance.value)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        instance_dates = CourseDate.objects.get(course=instance)

        for date in dates:
            instance_dates.day = date['day']
            instance_dates.hour = date['hour']
            instance_dates.save()
        
        return instance