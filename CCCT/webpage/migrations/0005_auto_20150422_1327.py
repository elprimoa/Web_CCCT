# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_auto_20150422_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='abstract',
            field=models.CharField(default='', max_length=300),
            preserve_default=True,
        ),
    ]
