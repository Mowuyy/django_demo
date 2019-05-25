# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('image', models.CharField(max_length=50, default='测试')),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('hcontent', models.CharField(max_length=100)),
                # ('test', models.CharField(max_length=100)),
                # ('test01', models.CharField(max_length=100)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booktest.BookInfo')),
            ],
            options={
                'db_table': 'heroinfo',
            },
        ),
    ]
