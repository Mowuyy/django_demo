# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroinfo',
            name='test',
            field=models.CharField(max_length=100, default=''),
            preserve_default=False,
        ),
    ]
