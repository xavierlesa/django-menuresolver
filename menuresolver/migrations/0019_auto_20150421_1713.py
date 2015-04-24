# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0018_item_link_to_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='link_to_email',
            field=models.CharField(help_text=b'Para tomar este link dejar campo URL y objetos relacionados vacios', max_length=255, null=True, verbose_name=b'Link a Mail', blank=True),
            preserve_default=True,
        ),
    ]
