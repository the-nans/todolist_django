from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.decorators import renderer_classes
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin,
                          GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes([JSONRenderer, BrowsableAPIRenderer])
