from django.urls import path, include
from schedule import views

urlpatterns = [
    path('<int:year>/<str:month>/', views.diary, name='diary'),
]