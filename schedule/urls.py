from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_list, name='schedules'),
    path('<int:pk>/', views.calendar_detail, name='schedule_detail'),
    path('<int:calendar_pk>/notes/', views.note_list, name='note_list'),
]