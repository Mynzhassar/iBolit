import logging

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins

from core.models import Department, Doctor, Consultant
from core.serializers import DepartmentSerializer, DepartmentDetailedSerializer, DoctorSerializer, ConsultantSerializer

logger = logging.getLogger(__name__)


class DepartmentViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    queryset = Department.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list':
            return DepartmentSerializer
        if self.action == 'retrieve':
            return DepartmentDetailedSerializer

        return DepartmentSerializer


class DoctorViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (IsAuthenticated,)


class ConsultantViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer
    permission_classes = (IsAuthenticated,)
