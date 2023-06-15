from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import CustomUserModel
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    list of users
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = CustomUserModel.objects.all()
