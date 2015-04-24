# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0016_auto_20150420_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_link',
            field=models.BooleanField(default=True, verbose_name=b'Es link'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='link_target',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name=b'Modo de apertura', choices=[(None, 'nada'), (b'_blank', 'Nueva pesta\xf1a'), (b'_new', 'Nueva ventana')]),
            preserve_default=True,
        ),
    ]
