from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers import ClinicSerializer
from core.models import Clinic


class ClinicCreateListDelete(APIView):

    http_method_names = ['get', 'post']

    def get(self, request):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)