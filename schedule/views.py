from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import calendar
from calendar import HTMLCalendar
import datetime
from time import gmtime, strftime
from schedule.models import Schedule

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

def diary(request):
    return render (request, 'diary.html')