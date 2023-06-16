from rest_framework.serializers import CharField
from djoser.conf import settings
from djoser.serializers import UserCreateSerializer, UserSerializer
from hashid_field.rest import HashidSerializerCharField

from .models import CustomUserModel


class CustomUserCreateSerializer(UserCreateSerializer):
    """
    user register serializer
    """
    first_name = CharField(max_length=150, required=False)
    last_name = CharField(max_length=150, required=False)
    phone = CharField(max_length=13, required=False)

    class Meta:
        model = CustomUserModel
        fields = tuple(CustomUserModel.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            "password",
            "first_name",
            "last_name",
            "phone"
        )


class CustomUserSerializer(UserSerializer):
    """
    user serializer
    """
    id = HashidSerializerCharField(source_field='user.CustomUserModel.id')
    class Meta:
        model = CustomUserModel
        fields = tuple(CustomUserModel.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
            "first_name",
            "last_name",
            "phone"
        )
        read_only_fields = (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
        )