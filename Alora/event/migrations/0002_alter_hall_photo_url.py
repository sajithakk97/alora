# Generated by Django 3.2.7 on 2025-01-23 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='photo_url',
            field=models.FileField(upload_to=''),
        ),
    ]
