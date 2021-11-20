from abc import ABC

from rest_framework.serializers import HyperlinkedModelSerializer, Serializer
from rest_framework import serializers
from user.models import User
from todo_project.models import ToDoNote, Project


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        # fields = '__all__'


class ProjectModelSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=32)
    link = serializers.URLField(allow_blank=True)
    user = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='username'
    )


    class Meta:
        model = Project
        fields = '__all__'


class ToDoNoteModelSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        many=False,
        queryset=User.objects.all(),
        slug_field='username'
    )

    project = serializers.SlugRelatedField(
        many=False,
        queryset=Project.objects.all(),
        slug_field='link'
    )


    class Meta:
        model = ToDoNote
        fields = '__all__'
