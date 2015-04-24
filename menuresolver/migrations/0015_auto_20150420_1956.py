# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0014_auto_20150420_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='wrap_tag',
            field=models.CharField(default=b'li', max_length=255, verbose_name=b'Tag HTML'),
            preserve_default=True,
        ),
    ]
