# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('mezzanine_page_comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_count', models.IntegerField(default=0, editable=False)),
                ('page', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pages.RichTextPage')),
            ],
        ),
        migrations.RemoveField(
            model_name='pagewithcomments',
            name='richtextpage_ptr',
        ),
        migrations.DeleteModel(
            name='PageWithComments',
        ),
    ]
