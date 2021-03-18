from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dailyreports/', views.dailyreports,name='dailyreports'),
    path('monthlyreports/',views.monthlyreports,name='monthlyreports'),
]
