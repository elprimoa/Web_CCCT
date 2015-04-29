# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('part', models.ForeignKey(to='webpage.Member')),
                ('proj', models.ForeignKey(to='webpage.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='abstract',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
