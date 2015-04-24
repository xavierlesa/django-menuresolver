# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0013_auto_20150420_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='attrs_tag',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Atributos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='class_tag',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Class', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='wrap_tag',
            field=models.CharField(default=b'ul', max_length=255, verbose_name=b'Tag HTML'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menu',
            name='attrs_tag',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Atributos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menu',
            name='class_tag',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name=b'Class', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menu',
            name='wrap_tag',
            field=models.CharField(default=b'ul', max_length=255, verbose_name=b'Tag HTML'),
            preserve_default=True,
        ),
    ]