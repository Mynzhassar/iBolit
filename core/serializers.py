from rest_framework import serializers
from core.models import Clinic


def validate_title(title):
    for char in title:
        if not char.isalpha(): raise ValueError(f'{char} character is not allowed')


class ClinicSerializer(serializers.Serializer):
    title = serializers.CharField()
    rating = serializers.IntegerField()
    status = serializers.IntegerField()

    def create(self, validated_data):
        return Clinic(**validated_data).save()
