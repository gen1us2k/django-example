from __future__ import unicode_literals

from django.db import models
from base.models import AbstractDateTimeModel


class Task(AbstractDateTimeModel):
    assignee = models.ForeignKey('users.User', related_name='assignee')
    created_by = models.ForeignKey('users.User', related_name='created_by')
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
