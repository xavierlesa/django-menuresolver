# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menuresolver', '0022_menuitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='menu',
            field=modelcluster.fields.ParentalKey(related_name='items', to='menuresolver.Menu'),
            preserve_default=True,
        ),
    ]
