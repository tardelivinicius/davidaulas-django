from rest_framework import serializers, status
from student.models import Student, Address, Phone
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['telephone_residential',
                  'telephone_mobile'   
                 ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address',
                  'number'
                 ]


class StudentSerializer(serializers.ModelSerializer):
    address_student = AddressSerializer(many=True)
    phone_student = PhoneSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id',
                  'email',
                  'name',
                  'name_responsible',
                  'dtInc',
                  'address_student',
                  'phone_student',
                  'status' 
                 ]

       
    def create(self, validated_data):

        adresses = validated_data.pop('address_student')
        phones = validated_data.pop('phone_student')
        student = Student.objects.create(**validated_data)

        for address in adresses:
            Address.objects.create(student=student, **address)

        for phone in phones:
            Phone.objects.create(student=student, **phone)

        return student

    def update(self, instance, validated_data):

        adresses = validated_data.pop("address_student", [])
        phones = validated_data.pop("phone_student")
        
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.name_responsible = validated_data.get('name_responsible', instance.name_responsible)
        instance.save()
        
        instance_address = Address.objects.filter(student=instance).count()
        instance_phones = Phone.objects.filter(student=instance).count()
               
        if instance_address == 0:
            for address in adresses:
                Address.objects.create(student=instance, **address)
        else:
            instance_address = Address.objects.get(student=instance)
            for address in adresses:
                instance_address.address = address['address']
                instance_address.number = address['number']
                instance_address.save()
        
        
        if instance_phones == 0:
            for phone in phones:
                Phone.objects.create(student=instance, **phone)
        else:
            instance_phones = Phone.objects.get(student=instance)
            for phone in phones:
                instance_phones.telephone_residential = phone['telephone_residential']
                instance_phones.telephone_mobile = phone['telephone_mobile']
                instance_phones.save()

        return instance


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name']