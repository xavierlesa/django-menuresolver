# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0010_auto_20150420_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='wrap_tag',
            field=models.CharField(default=b'<ul class="%(class_tag)" %(attrs_tag)>%(items)</ul>', max_length=255),
            preserve_default=True,
        ),
    ]
