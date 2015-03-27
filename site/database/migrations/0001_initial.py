# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('title', models.CharField(default=None, max_length=50, serialize=False, primary_key=True)),
                ('title_slug', models.SlugField(default=b'')),
                ('artist', models.CharField(default=b'', max_length=50)),
                ('speed', models.CharField(default=b'', max_length=10, choices=[(b'S', b'Slow'), (b'FS', b'Fast/Slow'), (b'F', b'Fast')])),
                ('lyrics', models.TextField(null=True, blank=True)),
                ('doc', models.FileField(default=b'', upload_to=b'doc')),
                ('pdf', models.FileField(default=b'', upload_to=b'pdf')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='song',
            name='themes',
            field=models.ManyToManyField(to='database.Theme'),
            preserve_default=True,
        ),
    ]
