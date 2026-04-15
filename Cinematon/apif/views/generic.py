from rest_framework.generics import CreateAPIView
from ..serializers import UserSerializer
from ..models import User


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer