import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer
from users.models import MainUser

logger = logging.getLogger(__name__)

class RegisterUserAPIView(APIView):
    http_method_names = ['POST']

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"{self.request.user} registered as: {serializer.data.get('username')}")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MainUser.objects.all()
