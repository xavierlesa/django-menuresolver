# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('menuresolver', '0009_auto_20150417_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='url',
            field=models.URLField(null=True, verbose_name=b'URL alternativa', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_text',
            field=models.CharField(max_length=255, verbose_name=b'Titulo del item'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(max_length=255),
            preserve_default=True,
        ),
    ]
