# Generated by Django 3.2.13 on 2022-06-15 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=10000000)),
                ('created_At', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
