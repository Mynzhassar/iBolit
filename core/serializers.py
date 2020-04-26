from rest_framework import serializers

from core.models import Clinic, Department, Doctor, Consultant, Service, Order
from utils.constants import *


def rating_validator(rating):
    if rating not in range(10): raise ValueError(f"{rating} rating is invalid")


def floor_validator(floor):
    if floor not in range(1, 4): raise ValueError(f"{floor} floor is invalid")


def direction_validator(self, value):
    if value < 1 or value > len(CLINIC_DEPARTMENTS) or not isinstance(value, int):
        raise serializers.ValidationError(f'Departments type directions: {CLINIC_DEPARTMENTS}')


class ClinicSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    rating = serializers.IntegerField(validators=[rating_validator])

    class Meta:
        model = Clinic
        fields = ('id', 'title', 'address', 'rating', 'status')


class DepartmentSerializer(serializers.ModelSerializer):
    clinic_id = serializers.IntegerField(write_only=True)
    floor = serializers.IntegerField(required=True, validators=[floor_validator])
    direction = serializers.IntegerField(validators=[direction_validator])

    class Meta:
        model = Department
        fields = ('id', 'clinic_id', 'direction', 'floor')


class DepartmentDetailedSerializer(serializers.ModelSerializer):
    class Meta(DepartmentSerializer.Meta):
        fields = DepartmentSerializer.Meta.fields + ('clinic',)


class DoctorSerializer(serializers.Serializer):
    clinic = serializers.IntegerField(write_only=True)
    department = serializers.IntegerField(write_only=True)
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
    clinic = serializers.IntegerField(write_only=True)
    department = serializers.IntegerField(write_only=True)
    surname = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)

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
    clinic = ClinicSerializer()

    class Meta:
        model = Service
        fields = ('id', 'title', 'price', 'cabinet', 'clinic')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'doctor', 'service', 'consultant', 'payment_type', 'date', 'time')
