from django.contrib import admin
from.models import Schedule, ClientEventNote
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Schedule)
class ScheduleAdmin(SummernoteModelAdmin):

    list_display = ('client', 'slug', 'status')
    search_fields = ['client', 'carer']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('client', 'start')}
    summernote_fields = ('carer',)

# Register your models here.
admin.site.register(ClientEventNote)