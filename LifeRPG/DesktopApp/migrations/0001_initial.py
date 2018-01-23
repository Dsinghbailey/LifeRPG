# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-15 08:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aspect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('science', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MissionAspects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DesktopApp.Aspect')),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DesktopApp.Mission')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('xp', models.IntegerField()),
                ('hearts', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAspect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('aspect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DesktopApp.Aspect')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserLevelUps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levelup_time', models.DateField()),
                ('level', models.IntegerField()),
                ('aspect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DesktopApp.Aspect')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserMissionRatings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_time', models.DateField()),
                ('rating', models.IntegerField()),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DesktopApp.Mission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
