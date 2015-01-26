# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='speed',
            field=models.CharField(default=b'', max_length=10, choices=[(b'S', b'Slow'), (b'FS', b'Fast/Slow'), (b'F', b'Fast')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(default=None, max_length=50, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
