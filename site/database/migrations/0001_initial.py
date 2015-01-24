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
                ('title', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('artist', models.CharField(max_length=50, null=True)),
                ('themes', models.TextField(null=True)),
                ('speed', models.CharField(max_length=10, null=True, choices=[(b'S', b'Slow'), (b'FS', b'Fast/Slow'), (b'F', b'Fast')])),
                ('lyrics', models.TextField(null=True)),
                ('doc', models.FileField(default=b'', upload_to=b'doc')),
                ('pdf', models.FileField(default=b'', upload_to=b'pdf')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
