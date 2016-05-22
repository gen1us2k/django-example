# -*- coding: utf-8 -*-
import json
from django.db import transaction
from django.db.transaction import TransactionManagementError

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from billing.models import TaskExpense
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

    def create(self, request, *args, **kwargs):
        request.data['created_by'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @detail_route(methods=['POST', 'GET'])
    def assign(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, assignee=None)
        except Task.DoesNotExist:
            return Response(json.dumps({"message": "Already taken"}), status=status.HTTP_400_BAD_REQUEST)

        expense, created = TaskExpense.objects.get_or_create(
            task=task,
            executor_id=request.user.pk,
            money=task.money)

        if created:
            with transaction.atomic():
                request.user.update_balance(u"Взял задачу", task.money, task=task)

        Task.objects.filter(pk=pk, assignee=None).update(assignee=request.user)
        return Response(json.dumps({'message': "Taken"}), status=status.HTTP_200_OK)
