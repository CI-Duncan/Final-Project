# Generated by Django 4.2.14 on 2024-08-01 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_schedule_content_schedule_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]