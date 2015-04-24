# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0025_auto_20150422_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='class_tag',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Class'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(related_name='items', to='menuresolver.Menu'),
            preserve_default=True,
        ),
    ]
