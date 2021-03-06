# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0006_pageranking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster', models.BooleanField()),
                ('pagerank', models.BooleanField()),
                ('query', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pageranking',
            name='alpha',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pageranking',
            name='threshold',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
