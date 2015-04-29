# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_auto_20150422_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='ctype',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=50),
            preserve_default=True,
        ),
    ]
