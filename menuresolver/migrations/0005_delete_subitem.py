# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0004_auto_20150417_1925'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubItem',
        ),
    ]
