import traceback

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from .models import Users, WorkerUser


class UsersAuthSerializers(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='Users-detail-detail', )

    class Meta:
        model = Users
        fields = ['url', 'auth', 'name', 'username']


class UsersAuthDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['auth']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password', 'name']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        raise_errors_on_nested_writes('create', self, validated_data)
        ModelClass = self.Meta.model

        # Remove many-to-many relationships from validated_data.
        # They are not valid arguments to the default `.create()` method,
        # as they require that the instance has already been saved.
        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)

        try:
            instance = ModelClass._default_manager.create(**validated_data)
        except TypeError:
            tb = traceback.format_exc()
            msg = (
                    'Got a `TypeError` when calling `%s.%s.create()`. '
                    'This may be because you have a writable field on the '
                    'serializer class that is not a valid argument to '
                    '`%s.%s.create()`. You may need to make the field '
                    'read-only, or override the %s.create() method to handle '
                    'this correctly.\nOriginal exception was:\n %s' %
                    (
                        ModelClass.__name__,
                        ModelClass._default_manager.name,
                        ModelClass.__name__,
                        ModelClass._default_manager.name,
                        self.__class__.__name__,
                        tb
                    )
            )
            raise TypeError(msg)


class WorkUserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='WorkViewSet-detail')

    class Meta:
        model = WorkerUser
        fields = [
            'url',
            "id",
            "name",
            # "phone",
            "password",
            "mail",
            "ctime",
            "status",
            "sort",
            "jobs",
            "branch",
            # "usercard",
            "jobnature",
            "tryout",
            "usernumber",
            "deleted",
            "years",
            "month",
            "day",
            "zzface",
            "ztimeday",
            "ztime",
            "lztime",
            "salary",
            "sysalary",
            "sbbase",
            "gjjbase",
            "znedu",
            "jxedu",
            "zfdklx",
            "zfzj",
            "dbyl",
            "sylr"]
