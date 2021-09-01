# Generated by Django 3.1.7 on 2021-09-01 02:00

import api_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=api_app.models.upload_path)),
            ],
        ),
    ]
