# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('funded', models.CharField(max_length=100)),
                ('abstract', models.CharField(max_length=5000)),
                ('responsible', models.ForeignKey(to='webpage.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
