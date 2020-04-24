import logging
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.serializers import UserSerializer
from users.models import MyUser

logger = logging.getLogger(__name__)


class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.debug(f'{serializer.instance} user created')
        logger.info(f'{serializer.instance} user created')
        logger.warning(f'{serializer.instance} user created')
        logger.error(f'{serializer.instance} user created')
        logger.critical(f'{serializer.instance} user created')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MyUser.objects.all()
