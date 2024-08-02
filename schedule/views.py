from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Schedule
import calendar
from calendar import HTMLCalendar
import datetime
from time import gmtime, strftime


#Create your views here.
# def diary(request, year, month,):
#     mode = "Testing"
#     month = month.capitalize()
#     #Convert month to number
#     month_num = list(calendar.month_name).index(month)
#     month_num = int(month_num)

#     #Create Calendar for display
#     cal = HTMLCalendar().formatmonth(
#         year, month_num
#     )

#     #Get time
#     time = strftime("%H:%M", gmtime())
#     #Get current date
#     today = datetime.date.today()


#     return render(request,
#                     'diary.html', {
#                     "mode": mode,
#                     "time": time,
#                     "today": today,
#                     "month": month,
#                     "year": year,
#                     "month_num": month_num,
#                     "cal": cal,
#                     })

class Diary(generic.ListView):
    model = Schedule
    queryset = Schedule.objects.filter()
    template_name = 'schedule/index.html'
    context_object_name = 'schedules'