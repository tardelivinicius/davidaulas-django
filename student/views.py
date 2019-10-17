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
        queryset = Student.objects.prefetch_related(
            'phone_student',
            Prefetch(
                'address_student',
                queryset=Address.objects.all()
            )
        )
        return queryset

    def create(self, request):
        serializer = self.get_serializer(data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        student = get_object_or_404(self.get_queryset().filter(pk=pk))
        serializer = self.get_serializer(student, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        student = get_object_or_404(Student.objects.filter(pk=pk))
        student.status = 3
        student.save()

        return Response({"detail:" "success"}, status=status.HTTP_200_OK)