# Generated by Django 4.2.14 on 2024-07-31 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('cal_id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evnt_notes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblschedule',
            },
        ),
    ]