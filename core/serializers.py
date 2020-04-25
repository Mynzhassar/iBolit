from rest_framework import serializers
from utils.constants import *
from core import models
from users.serializers import UserSerializer


class ClinicShortSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = models.Clinic
        fields = ('id', 'title', 'address', 'rating', 'status')

    def validate_title(title):
        for char in title:
            if not char.isalpha():
                raise ValueError(f'{char} character is not allowed')


class ClinicSerializer(ClinicShortSerializer):
    class Meta(ClinicShortSerializer.Meta):
        fields = ClinicShortSerializer.Meta.fields + ('info',)


class DepartmentSerializer(serializers.ModelSerializer):
    clinic = ClinicShortSerializer(read_only=True)
    direction_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Department
        fields = ('id', 'direction_name','direction', 'floor', 'clinic',)

    def get_direction_name(self, obj):
        types_dict = dict(CLINIC_DEPARTMENTS)
        if types_dict[obj.direction]:
            return types_dict[obj.direction]
        return ''

    def validate_direction(self, value):
        if value < 1 or value > len(CLINIC_DEPARTMENTS) or not isinstance(value, int):
            raise serializers.ValidationError(f'Departments type directions: {CLINIC_DEPARTMENTS}')
        return value

    def validated_floor(self, value):
        if value <= 0:
            raise serializers.ValidationError('Department floor must be greater than 0')
        return value


class DoctorSerializer():
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = models.Doctor
        fields = ('id', 'name', 'surname', 'job_title', 'cabinet', 'department',)

class ConsultantSerializer(serializers.Serializer):
    department = DepartmentSerializer(read_only=True)
    surname = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)

    def create(self, validated_data):
        consultant = models.Consultant(**validated_data)
        consultant.save()
        return consultant

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


class ServiceSerializer(serializers.ModelSerializer):
    clinic = ClinicShortSerializer()

    class Meta:
        model = models.Service
        fields = ('id', 'title', 'price', 'cabinet', 'clinic')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ('id', 'doctor', 'service', 'consultant', 'payment_type', 'date', 'time')



