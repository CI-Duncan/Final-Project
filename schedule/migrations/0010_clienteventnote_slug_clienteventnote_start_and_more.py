# Generated by Django 4.2.14 on 2024-08-06 14:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0009_alter_schedule_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteventnote',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='clienteventnote',
            name='start',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_start', to='schedule.schedule'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]