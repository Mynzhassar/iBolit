from rest_framework import serializers
from users.models import MyUser, Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'is_superuser', 'password',)

    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = '__all__'
        read_only_fields = ('user', )

    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance
