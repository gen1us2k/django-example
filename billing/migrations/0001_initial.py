# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 13:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoneyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('reason', models.CharField(max_length=255)),
                ('debit', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('credit', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
