# Generated by Django 4.2.14 on 2024-08-06 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_remove_clienteventnote_cal_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clienteventnote',
            name='event_start_time',
        ),
        migrations.AddField(
            model_name='clienteventnote',
            name='cal_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_notes', to='schedule.schedule'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clienteventnote',
            name='start',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_start', to='schedule.schedule'),
            preserve_default=False,
        ),
    ]