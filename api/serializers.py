# -*- coding: utf-8 -*-
from rest_framework import serializers
from django_example.users.models import User
from task.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'first_name', 'last_name', 'username', 'email', 'id')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description')
