from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView,\
    UpdateAPIView, get_object_or_404, DestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from todo_project.models import User, ToDoNote, Project
from todo_project.serializers import UserModelSerializer, ToDoNoteModelSerializer, ProjectModelSerializer
from todo_project.filters import ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ToDoNoteModelViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin,
                          GenericViewSet):
    """
    модель ToDo доступны все варианты запросов; при удалении не удалять ToDo, а выставлять признак, что оно закрыто;
    добавить фильтрацию по проекту; для постраничного вывода установить размер страницы 20.

    """
    queryset = ToDoNote.objects.all()
    serializer_class = ToDoNoteModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project']


    pagination_class = ToDoLimitOffsetPagination

    def destroy(self, request, pk=None):
        note = get_object_or_404(ToDoNote, pk=pk)
        note.done = True
        note.save()
        serializer = ToDoNoteModelSerializer(note, context={'request': request})
        return Response(serializer.data)

class ProjectModelViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin,
                          GenericViewSet):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

