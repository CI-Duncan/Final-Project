from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views import generic
from .models import ClientEventNote, Schedule
import calendar
from calendar import HTMLCalendar
from datetime import datetime
import logging
logger = logging.getLogger(__name__)
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
    model = ClientEventNote
    template_name = "schedule/diary.html"
    context_object_name = "events"

    def get_queryset(self):
        return ClientEventNote.objects.all().order_by('-note_created')

def schedule_details(request, slug=None):
    """
    Displays individual ClientEventNote based on the Schedule's start date.
    Redirects to the diary view if slug is missing.
    """
    if not slug:
        # Redirect to the diary view if slug is missing
        return redirect('diary')

    try:
        # Convert slug to a date object
        date_str = slug.split("-")  # Splitting the slug to extract date components
        if len(date_str) != 3 or not all(x.isdigit() for x in date_str):
            raise ValueError("Invalid date format in slug")
            
        date_to_filter = datetime.strptime("-".join(date_str), "%Y-%m-%d").date()

        # Retrieve the ClientEventNote based on the start date of the related Schedule
        event = get_object_or_404(ClientEventNote.objects.filter(cal_id__start=date_to_filter))
    except ValueError:
        logger.error(f"Invalid date format in slug: {slug}")
        return HttpResponse("Invalid date format in slug.", status=400)
    
    return render(
        request,
        "schedule/diary.html",
        {"event": event},
    )