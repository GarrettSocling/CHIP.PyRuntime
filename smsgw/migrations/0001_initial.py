# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InboxSMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=20)),
                ('received_date', models.DateTimeField()),
                ('text', models.CharField(max_length=1024)),
            ],
        ),
    ]