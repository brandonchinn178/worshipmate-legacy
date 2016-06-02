# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 06:00
from __future__ import unicode_literals

import database.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='song',
            name='doc',
            field=models.FileField(upload_to=database.models.doc_upload_file, validators=[database.models.doc_file_validator]),
        ),
        migrations.AlterField(
            model_name='song',
            name='lyrics',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='pdf',
            field=models.FileField(upload_to=database.models.pdf_upload_file, validators=[database.models.pdf_file_validator]),
        ),
        migrations.AlterField(
            model_name='song',
            name='speed',
            field=models.CharField(choices=[(b'', b''), (b'F', b'Fast'), (b'S', b'Slow'), (b'FS', b'Fast/Slow')], max_length=2),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='title_slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='song',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='theme',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
