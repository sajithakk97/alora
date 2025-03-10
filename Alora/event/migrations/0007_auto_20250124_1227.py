# Generated by Django 3.2.7 on 2025-01-24 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_decoration_decoration_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='decoration',
            new_name='decoration_model',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='event_data',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='customization',
            new_name='suggestion',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='other',
        ),
        migrations.AddField(
            model_name='booking',
            name='include_decoration',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='include_food',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='payment_status',
            field=models.CharField(blank=True, default='pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='photography_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=1000, max_digits=10, null=True),
        ),
    ]
