from django.urls import path
from . import views

urlpatterns = [
    path('', views.Diary.as_view(), name='diary'),
    path('<slug:slug>/', views.schedule_details, name='schedule_details'),
]