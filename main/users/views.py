from rest_framework import generics
from rest_framework.permissions import AllowAny

from main.users.models import MyUser
from main.users.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):

    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get_queryset(self):
        return MyUser.objects.all()

    def get_serializer_class(self):
        return UserSerializer
