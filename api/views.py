# -*- coding: utf-8 -*-

from rest_framework import viewsets
from .serializers import UserSerializer, TaskSerializer
from django_example.users.models import User
from task.models import Task


class ExecutorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(user_type=User.EXECUTOR)
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(user_type=User.CUSTOMER)
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
