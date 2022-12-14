# Generated by Django 4.0.6 on 2022-11-13 14:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_postmodel_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='metadata',
            field=models.FileField(null=True, upload_to='files/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['csv', 'json'])]),
        ),
    ]
