# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0023_auto_20150422_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='menu',
            field=models.ForeignKey(related_name='menu', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='menuresolver.Menu', null=True),
            preserve_default=True,
        ),
    ]
