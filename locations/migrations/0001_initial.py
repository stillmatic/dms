# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('check_time', models.DateTimeField(verbose_name='User checkin date/time', default=datetime.datetime.now, blank=True)),
                ('check_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
