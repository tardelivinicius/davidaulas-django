from rest_framework import serializers, status
from student.models import Student, Address, Phone
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = [
                  'id',
                  'telephone_residential',
                  'telephone_mobile'
                 ]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
                  'id',
                  'address',
                  'number'
                 ]


class StudentSerializer(serializers.ModelSerializer):
    address_student = AddressSerializer(many=True)
    phone_student = PhoneSerializer(many=True)

    class Meta:
        model = Student
        fields = [
                  'id',
                  'email',
                  'name',
                  'name_responsible',
                  'date_joined',
                  'address_student',
                  'phone_student',
                  'status'
                 ]


    def create(self, validated_data):
        adresses = validated_data.pop('address_student', None)
        phones = validated_data.pop('phone_student', None)
        instance = Student(**validated_data)
        instance.save()
        self._save_address(instance, adresses)
        self._save_phones(instance, phones)
        return instance

    def update(self, instance, validated_data):
        adresses = validated_data.pop("address_student", None)
        phones = validated_data.pop("phone_student", None)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.name_responsible = validated_data.get('name_responsible', instance.name_responsible)
        instance.save()
        self._save_address(instance, adresses)
        self._save_phones(instance, phones)
        return instance

    def _save_address(self, instance, adresses):
        if adresses not in [None, '']:
            for address in adresses:
                if 'id' in address:
                    instance_address = Address(pk=address['id'])
                    instance_address.address = badge_language['address']
                    instance_address.number = badge_language['number']
                    instance_address.save()
                else:
                    address = Address(address=address['address'],
                                      number=address['number'],
                                      student=instance)
                    address.save()

    def _save_phones(self, instance, phones):
        if phones not in [None, '']:
            for phone in phones:
                if 'id' in phone:
                    instance_phones = Phone(pk=phone['id'])
                    instance_phones.telephone_residential = phone['telephone_residential']
                    instance_phones.telephone_mobile = phone['telephone_mobile']
                    instance_phones.save()
                else:
                    phone = Phone(student=instance,
                            telephone_residential=phone['telephone_residential'],
                            telephone_mobile=phone['telephone_mobile']
                                 )
                    phone.save()


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name']