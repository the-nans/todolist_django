import datetime

from django.db import models
from user.models import User
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=32)
    link = models.URLField(blank=True)
    user = models.ManyToManyField(User, blank=True)
    description = models.TextField(blank=True)


class ToDoNote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, blank=True, default=1)
    text = models.TextField()
    date_added = models.DateField(auto_now=True)
    date_edited = models.DateField(auto_now=True)
    done = models.BooleanField(default=False)
    author = models.OneToOneField(User, on_delete=models.PROTECT, blank=False)
