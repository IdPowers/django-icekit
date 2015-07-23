# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import icekit.models


class Migration(migrations.Migration):

    dependencies = [
        ('icekit', '0003_layout_content_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='content_types',
            field=models.ManyToManyField(help_text=b'Types of content for which this layout will be allowed.', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='layout',
            name='template_name',
            field=icekit.models.TemplateNameField(max_length=255, verbose_name='template', choices=[(b'', b'')]),
            preserve_default=True,
        ),
    ]