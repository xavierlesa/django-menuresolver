# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0019_auto_20150421_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='link_target',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name=b'Modo de apertura', choices=[(None, 'nada'), (b'_blank', 'Nueva pesta\xf1a'), (b'_new', 'Nueva ventana'), (b'_top', 'Arriba')]),
            preserve_default=True,
        ),
    ]
