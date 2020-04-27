import logging

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from core import models, serializers, permissions

logger = logging.getLogger(__name__)


class ClinicViewSet(viewsets.ModelViewSet):
    queryset = models.Clinic.objects.all()
    serializer_class = serializers.ClinicDetailedSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ClinicSerializer
        return serializers.ClinicDetailedSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f"{self.request.user} created clinic: {serializer.data.get('username')}")
        return serializer.data

    @action(methods=['GET', 'POST'], detail=True)
    def departments(self, request, pk):
        if request.method == 'GET':
            clinic = get_object_or_404(models.Clinic, id=pk)
            res = serializers.DepartmentSerializer(models.Department.objects.filter(clinic_id=clinic.id), many=True)
            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            ##  clinic = models.Clinic.objects.get(id=self.kwargs['pk'])
            ##request.data['clinic_id'] = instance.id
            serializer = serializers.DepartmentDetailedSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created department: {serializer.data.get('username')}")
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True)
    def services(self, request, pk):
        if request.method == 'GET':
            clinic = get_object_or_404(models.Clinic, id=pk)
            res = serializers.ServiceDetailedSerializer(models.Service.objects.filter(clinic_id=clinic.id), many=True)
            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            #   request.data['project_id'] = instance.id
            serializer = serializers.ServiceDetailedSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created service: {serializer.data.get('username')}")
            return Response(serializer.errors)


class DepartmentDetailedViewSet(mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentDetailedSerializer
    permission_classes = (IsAuthenticated,)

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
            logger.info(f"{self.request.user} created doctor: {serializer.data.get('username')}")
            return Response(serializer.errors)

    @action(methods=['GET', 'POST'], detail=True)
    def consultants(self, request, pk):
        if request.method == 'GET':
            department = get_object_or_404(models.Department, id=pk)
            res = serializers.ConsultantDetailedSerializer(
                models.Consultant.objects.filter(department_id=department.id),
                many=True)

            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = serializers.ConsultantDetailedSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created consultant: {serializer.data.get('username')}")
            return Response(serializer.errors)


class OrderToServiceViewSet(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceDetailedSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], detail=True)
    def orders(self, request, pk):
        if request.method == 'POST':
            instance = self.get_object()
            serializer = serializers.OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created order: {serializer.data.get('username')}")
            return Response(serializer.errors)


class OrderToDoctorViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], detail=True)
    def orders(self, request, pk):
        if request.method == 'POST':
            instance = self.get_object()
            serializer = serializers.OrderSerializer(data=request.data)
            if serializer.is_valid():
                #   serializer.client = request.user
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created order: {serializer.data.get('username')}")
            return Response(serializer.errors)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (permissions.UserPermission,)

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f"{self.request.user} created therapy document: {serializer.data.get('username')}")
        return serializer.data

    @action(methods=['GET', 'POST'], detail=True)
    def docs(self, request, pk):
        if request.method == 'GET':
            order = get_object_or_404(models.Order, id=pk)
            res = serializers.TherapyDocumentSerializer(models.TherapyDocument.objects.filter(order_id=order.id),
                                                        many=True)
            return Response(res.data)

        if request.method == 'POST':
            instance = self.get_object()
            serializer = serializers.TherapyDocumentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            logger.info(f"{self.request.user} created therapy document: {serializer.data.get('username')}")
            return Response(serializer.errors)


# class DepartmentViewSet(mixins.ListModelMixin,
#                         mixins.RetrieveModelMixin,
#                         mixins.CreateModelMixin,
#                         viewsets.GenericViewSet):
#     queryset = Department.objects.all()
#     permission_classes = (IsAuthenticated,)
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return DepartmentSerializer
#         if self.action == 'retrieve':
#             return DepartmentDetailedSerializer
#
#         return DepartmentSerializer
#
#
# class DoctorViewSet(mixins.ListModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.CreateModelMixin,
#                     viewsets.GenericViewSet):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer
#     permission_classes = (IsAuthenticated,)
#
#
#
# class ConsultantViewSet(mixins.ListModelMixin,
#                         mixins.RetrieveModelMixin,
#                         mixins.CreateModelMixin,
#                         viewsets.GenericViewSet):
#     queryset = Consultant.objects.all()
#     serializer_class = ConsultantSerializer
#     permission_classes = (IsAuthenticated,)
