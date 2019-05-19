from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from rest_framework import viewsets, status
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from student.models import Student, Address, Phone
from student.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        queryset = Student.objects.all()
        queryset = queryset.prefetch_related(
            'phone_student',
            Prefetch(
                'address_student',
                queryset=Address.objects.all()
            )
        )
        return queryset
    
    def create(self, request):

        address = request.data.pop("address_student", [])
        phones = request.data.pop("phone_student", [])

        student = Student.objects.create(**request.data)

        Address.objects.create(address, student=student)
        Phone.objects.create(phones, student=student)
        print(student)
        print(request.data)
        print(address)
        print(phones)

        return student
