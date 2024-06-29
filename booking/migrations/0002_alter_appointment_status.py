# Generated by Django 5.0.6 on 2024-06-23 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed'), ('canceled', 'Canceled'), ('reject', 'Reject')], default='pending', max_length=10),
        ),
    ]
