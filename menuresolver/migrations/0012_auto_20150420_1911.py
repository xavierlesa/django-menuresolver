# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0011_menu_wrap_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='attrs_tag',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menu',
            name='class_tag',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menu',
            name='wrap_tag',
            field=models.CharField(default=b'ul', max_length=255),
            preserve_default=True,
        ),
    ]
