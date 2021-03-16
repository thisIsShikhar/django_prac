from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request):
    return render(request,'accounts/dashboard.html')

def dailyreports(request):
    return render(request,'accounts/dailyreports.html')
    
def monthlyreports(request):
    return render(request,'accounts/monthlyreports.html')

