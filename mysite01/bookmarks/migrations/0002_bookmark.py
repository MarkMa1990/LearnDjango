# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('link', models.ForeignKey(to='bookmarks.Link')),
                ('user', models.ForeignKey(to='bookmarks.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
