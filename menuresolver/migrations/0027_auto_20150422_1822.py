# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0026_auto_20150422_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='class_tag',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Class'),
            preserve_default=True,
        ),
    ]
