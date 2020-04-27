from abc import ABC

from rest_framework import serializers
from users.serializers import UserSerializer
from core.models import Clinic, Department, Doctor, Consultant, Service, Order, TherapyDocument
from utils import validators


class ClinicSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    rating = serializers.IntegerField(validators=[validators.rating_validator])

    class Meta:
        model = Clinic
        fields = ('id', 'title', 'rating', 'status',)


class ClinicDetailedSerializer(ClinicSerializer):
    class Meta(ClinicSerializer.Meta):
        fields = ClinicSerializer.Meta.fields + ('address',)


class DepartmentSerializer(serializers.ModelSerializer):
    clinic_id = serializers.IntegerField(write_only=True)
    floor = serializers.IntegerField(required=True, validators=[validators.floor_validator])
    direction = serializers.IntegerField(validators=[validators.direction_validator])
    info = serializers.CharField(allow_blank=True)

    class Meta:
        model = Department
        fields = ('id', 'clinic_id', 'direction', 'floor', 'info')


class DepartmentDetailedSerializer(DepartmentSerializer):
    class Meta(DepartmentSerializer.Meta):
        fields = DepartmentSerializer.Meta.fields


class DoctorSerializer(serializers.Serializer):
    clinic_id = serializers.IntegerField(write_only=True)
    department_id = serializers.IntegerField(write_only=True)
    surname = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    experience = serializers.IntegerField(required=True)

    def create(self, validated_data):
        doctor = Doctor(**validated_data)
        doctor.save()
        return doctor

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.name = validated_data.get('name', instance.name)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.save()
        return instance


class ConsultantSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True, validators=[validators.phone_number_validator])


class ConsultantDetailedSerializer(serializers.Serializer):
    clinic_id = serializers.IntegerField(write_only=True)
    department_id = serializers.IntegerField(write_only=True)
    surname = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True, validators=[validators.phone_number_validator])

    def create(self, validated_data):
        consultant = Consultant(**validated_data)
        consultant.save()
        return consultant

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


class ServiceSerializer(serializers.ModelSerializer):
    clinic_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Service
        fields = ('id', 'title', 'clinic_id')


class ServiceDetailedSerializer(ServiceSerializer):
    class Meta(ServiceSerializer.Meta):
        fields = ServiceSerializer.Meta.fields + ('price', 'cabinet')


class OrderSerializer(serializers.ModelSerializer):
    client_id = serializers.IntegerField(write_only=True)
    doctor_id = serializers.IntegerField(write_only=True)
    service_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'client_id', 'doctor_id', 'service_id', 'payment_type', 'date', 'time')


class TherapyDocumentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = TherapyDocument
        fields = '__all__'
