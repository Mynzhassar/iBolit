import os
from django.core.exceptions import ValidationError
from rest_framework import serializers

from utils.constants import *

ALLOWED_EXTENSIONS = ['.jpg', '.png', '.docx']


def validate_document_size(value):
    if value.size > 10000000:
        raise ValidationError(f'max file size is: 10Mb')


def validate_document_extension(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in ALLOWED_EXTENSIONS:
        raise ValidationError(f'not allowed file ext, allowed: {ALLOWED_EXTENSIONS}')


def rating_validator(rating):
    if rating not in range(10): raise ValueError(f"{rating} rating is invalid")


def floor_validator(floor):
    if floor not in range(1, 4): raise ValueError(f"{floor} floor is invalid")


def direction_validator(value):
    if value < 1 or value > len(CLINIC_DEPARTMENTS) or not isinstance(value, int):
        raise serializers.ValidationError(f'Departments type directions: {CLINIC_DEPARTMENTS}')


def phone_number_validator(phone_number):
    if len(phone_number) != 11: raise ValueError("Phone number must contain 11 digits")
    country = phone_number[0]

    if country != '8': raise ValueError(f"{country} is invalid code")
    operator = phone_number[1] + phone_number[2] + phone_number[3]

    if operator not in ['777', '707', '701', '702', '770']: raise ValueError(f"{operator} is invalid operator")


def password_validator(password):
    has_digit = False
    has_letter = False

    if len(password) < 8: raise ValueError("Password length must be at least 8")

    for char in password:
        if char.isdigit(): has_digit = True
        if char.isalpha(): has_letter = True

    if not has_digit: raise ValueError("Password must contain at least one digit")
    if not has_letter: raise ValueError("Password must contain at lest one letter")


def therapy_document_size(value):
    if value.size > 200000:
        raise ValidationError('invalid file size')


def therapy_document_extension(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in ALLOWED_EXTENSIONS:
        raise ValidationError(f'not allowed ext, allowed ({ALLOWED_EXTENSIONS})')
