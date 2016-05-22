# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 12:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, '\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a'), (2, '\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c')], default=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username'),
        ),
    ]
