from django.urls import path
from . import views

urlpatterns = [
    path('', views.Diary.as_view(), name='diary'),  # Ensure the view name is correct
]