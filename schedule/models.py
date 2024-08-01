from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Scheduled"), (1, "Completed"))


class Schedule (models.Model):
    cal_id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_notes"
    )
    carer = models.TextField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        db_table = "tblschedule"

class ClientEventNote (models.Model):
    cal_id = models.ForeignKey(
        Schedule, on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_notes"
    )
    notes = models.TextField()
    created_on = created_on = models.DateTimeField(auto_now_add=True)


