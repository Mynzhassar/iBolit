import logging

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.serializers import *

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def clinic_list(request):
    if request.method == 'GET':
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ClinicDetailedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'"{serializer.instance}" clinic created')
            logger.info(f'"{serializer.instance}" clinic created')
            logger.warning(f'"{serializer.instance}" clinic created')
            logger.error(f'"{serializer.instance}" clinic created')
            logger.critical(f'"{serializer.instance}" clinic created')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def clinic_detail(request, pk):
    try:
        clinic = Clinic.objects.get(id=pk)
    except Clinic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClinicDetailedSerializer(clinic)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ClinicDetailedSerializer(instance=clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        clinic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
