from rest_framework.serializers import HyperlinkedModelSerializer
from user.models import User
from todo_project.models import ToDoNote, Project


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # fields = '__all__'


class ProjectModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Project
        # fields = ['username', 'first_name', 'last_name', 'email']
        fields = '__all__'


class ToDoNoteModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDoNote
        # fields = ['username', 'first_name', 'last_name', 'email']
        fields = '__all__'

    project = ProjectModelSerializer()