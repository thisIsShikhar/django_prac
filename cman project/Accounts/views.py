from Accounts.models import Entry
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request):
    return render(request,'accounts/dashboard.html')

def dailyreports(request):
    data=Entry.objects.all()
    return render(request,'accounts/dailyreports.html',{'entries':data})
    
def monthlyreports(request):
    return render(request,'accounts/monthlyreports.html')

