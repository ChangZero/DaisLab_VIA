# Generated by Django 4.0.6 on 2022-11-13 14:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_postmodel_image_alter_postmodel_metadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='data',
            field=models.FileField(blank=True, null=True, upload_to='datafiles/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['csv', 'json', 'zip'])]),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='metadata',
            field=models.FileField(null=True, upload_to='metafiles/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['csv', 'json', 'zip'])]),
        ),
    ]
