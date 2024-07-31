from . import views
from django.urls import path

urlpatterns = [
    path('<int:year>/<str:month>/', views.home, name='home'),
]