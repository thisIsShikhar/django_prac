from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('dailyreports/', views.dailyreports),
    path('monthlyreports/',views.monthlyreports),
]
