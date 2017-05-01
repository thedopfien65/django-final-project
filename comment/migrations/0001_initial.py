# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-01 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=250)),
                ('comment_author', models.CharField(max_length=40)),
                ('comment_date', models.DateTimeField(verbose_name=b'date published')),
                ('comment_rating', models.IntegerField()),
            ],
        ),
    ]