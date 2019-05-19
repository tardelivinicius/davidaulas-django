from rest_framework import serializers, status
from student.models import Student, Address


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    address_student = AddressSerializer(many=True, read_only=True)
    phone_student = PhoneSerializer(many=True, read_only=True)


    class Meta:
        model = Student
        fields = ['email',
                  'name',
                  'name_responsible',
                  'dtInc',
                  'address_student',
                  'phone_student',
                  'status' 
                 ]
        

