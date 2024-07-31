from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import calendar
from calendar import HTMLCalendar

#Create your views here.
def home(request, year, month):
    mode = "Testing"
    #Convert month to number
    month_num = list(calendar.month_name).index(month)

    return render(request,
                'diary.html', {
                    "mode": mode,
                    "year": year,
                    "month": month,
                    "month_num": month_num,
                })