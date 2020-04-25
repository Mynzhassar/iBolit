import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from core import serializers
from core import models
from core.permissions import UserPermission
from rest_framework.decorators import action

logger = logging.getLogger(__name__)


class ClinicViewSet(viewsets.ModelViewSet):
    queryset = models.Clinic.objects.all()
    serializer_class = serializers.ClinicSerializer
    permission_classes = (UserPermission,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ClinicShortSerializer
        return serializers.ClinicSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created clinic {serializer.data.get('title')}")
        return serializer.data

    @action(methods=['GET'], detail=False)
    def my(self, request):
        clinics = models.Clinic.objects.filter(creator_id=self.request.id)
        serializer = self.get_serializer(clinics, many=True)
        return Response(serializer.data)

    @action(methods=['GET', 'POST'], detail=True)
    def departments(self, request, pk):
        if request.method == 'GET':
            cl = get_object_or_404(models.Clinic, id=pk)
            res = serializers.DepartmentSerializer(models.Department.objects.filter(clinic_id=cl.id), many=True)

            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = serializers.DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created department: {serializer.data.get('direction')}")
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True)
    def services(self, request, pk):
        if request.method == 'GET':
            cl = get_object_or_404(models.Clinic, id=pk)
            res = serializers.ServiceSerializer(models.Service.objects.filter(clinic_id=cl.id), many=True)

            return Response(res.data)

        if request.method == 'POST':
            serializer = serializers.ServiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created service: {serializer.data.get('title')}")
            return Response(serializer.errors)


class DepartmentDetailViewSet(mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = (UserPermission,)

    @action(methods=['GET', 'POST'], detail=True)
    def doctors(self, request, pk):
        if request.method == 'GET':
            department = get_object_or_404(models.Department, id=pk)
            res = serializers.DoctorSerializer(models.Doctor.objects.filter(department_id=department.id), many=True)

            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = serializers.DoctorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created doctor: {serializer.data.get('name')}")
            return Response(serializer.errors)

        @action(methods=['GET', 'POST'], detail=True)
        def consultants(self, request, pk):
            if request.method == 'GET':
                department = get_object_or_404(models.Department, id=pk)
                res = serializers.ConsultantSerializer(models.Consultant.objects.filter(department_id=department.id),
                                                       many=True)

                return Response(res.data)

            if request.method == 'POST':
                instance = self.get_object()
                serializer = serializers.ConsultantSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                logger.info(f"{self.request.user} created consultant: {serializer.data.get('name')}")
                return Response(serializer.errors)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (UserPermission,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created order {serializer.data.get('id')}")
        return serializer.data


