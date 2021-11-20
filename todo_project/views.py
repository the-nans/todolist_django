from rest_framework.viewsets import ModelViewSet
from todo_project.models import User, ToDoNote, Project
from todo_project.serializers import UserModelSerializer, ToDoNoteModelSerializer, ProjectModelSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from djangorestframework_camel_case.render import CamelCaseJSONRenderer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class ToDoNoteModelViewSet(ModelViewSet):
    queryset = ToDoNote.objects.all()
    serializer_class = ToDoNoteModelSerializer

class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [BrowsableAPIRenderer, CamelCaseJSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

