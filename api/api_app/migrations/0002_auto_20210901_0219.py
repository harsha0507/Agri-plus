# Generated by Django 3.1.7 on 2021-09-01 02:19

import api_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=api_app.models.upload_path)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]