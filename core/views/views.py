import logging

from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.serializers import ClinicSerializer
from core.models import Clinic

logger = logging.getLogger(__name__)


class ClinicAPIView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post']

    def get(self, request):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'"{serializer.instance}" clinic created')
            logger.info(f'"{serializer.instance}" clinic created')
            logger.warning(f'"{serializer.instance}" clinic created')
            logger.error(f'"{serializer.instance}" clinic created')
            logger.critical(f'"{serializer.instance}" clinic created')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClinicDetailedApiView(APIView):
    permission_classes = (IsAuthenticated, )
    http_method_names = ['get', 'put', 'delete']

    def get_object(self, pk):
        try:
            return Clinic.objects.get(pk=pk)
        except Clinic.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        clinic = Clinic.objects.filter(pk=pk)
        serializer = ClinicSerializer(clinic, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        clinic = self.get_object(pk)
        serializer = ClinicSerializer(clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
