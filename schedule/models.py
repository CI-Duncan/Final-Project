from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Schedule (models.Model):
    cal_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="evnt_notes"
    )
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "tblschedule"
