from rest_framework import serializers
from django.contrib.auth.models import User


class UsersListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UsersSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'password']
