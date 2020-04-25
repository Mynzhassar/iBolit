import logging
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer, ProfileSerializer
from users.models import MyUser, Profile

logger = logging.getLogger(__name__)


class RegisterUserAPIView(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.debug(f'{serializer.instance} user created')
            logger.info(f'{serializer.instance} user created')
            logger.warning(f'{serializer.instance} user created')
            logger.error(f'{serializer.instance} user created')
            logger.critical(f'{serializer.instance} user created')
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = MyUser.objects.all()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class ProfileViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return self.queryset.all()
