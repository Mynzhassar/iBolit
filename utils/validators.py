import os
from django.core.exceptions import ValidationError

ALLOWED_EXTENSIONS = ['.jpg', '.png','.docx']


def validate_document_size(value):
    if value.size > 10000000:
        raise ValidationError(f'max file size is: 10Mb')


def validate_document_extension(value):
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in ALLOWED_EXTENSIONS:
        raise ValidationError(f'not allowed file ext, allowed: {ALLOWED_EXTENSIONS}')