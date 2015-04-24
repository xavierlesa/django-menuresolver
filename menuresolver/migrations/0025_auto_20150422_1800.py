# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0024_auto_20150422_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='item',
            name='sort_order',
            field=models.IntegerField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
