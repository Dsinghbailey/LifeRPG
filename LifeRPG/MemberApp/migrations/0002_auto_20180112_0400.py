# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-12 04:00
from __future__ import unicode_literals
from ..models import Aspect, IntakeQuestion, Mission, MissionAspect
from django.db import migrations
import csv
import os
import pdb


def load_aspects_from_csv(apps, schema_editor):
    f_name = os.path.join(os.path.dirname(__file__), 'data/aspects.csv')
    with open(f_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name'].lower()
            description = row['description']
            new_aspect = Aspect(name=name, description=description)
            new_aspect.save()


def load_intake_questions_from_csv(apps, schema_editor):
    f_name = os.path.join(os.path.dirname(__file__),
                          'data/intake_questions.csv')
    with open(f_name) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            aspect = Aspect.objects.get(name=row['aspect'].lower())
            question = row['question']
            new_question = IntakeQuestion(aspect=aspect,
                                          question=question)
            new_question.save()


def load_missions_from_csv(apps, schema_editor):
    f_name = os.path.join(os.path.dirname(__file__),
                          'data/missions.tsv')
    with open(f_name) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t')
        for row in reader:
            new_mission = Mission(image=row['image'],
                                  title=row['title'],
                                  content=row['content'],
                                  science='')
            new_mission.save()
            aspects = Aspect.objects.all()
            for aspect in aspects:
                if row[aspect.name] == '1':
                    mission_aspect = MissionAspect(mission=new_mission,
                                                   aspect=aspect)
                    mission_aspect.save()


class Migration(migrations.Migration):
    dependencies = [
        ('MemberApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_aspects_from_csv),
        migrations.RunPython(load_intake_questions_from_csv),
        migrations.RunPython(load_missions_from_csv)
    ]
