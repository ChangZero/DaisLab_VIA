# Generated by Django 4.0.6 on 2022-11-08 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='metadata',
            field=models.FileField(null=True, upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['csv', 'json'])]),
        ),
    ]
