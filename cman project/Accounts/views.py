from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request):
    return render(request,'accounts/dashboard.html')

def products(request):
    return render(request,'accounts/products.html')
    
def customers(request):
    return render(request,'accounts/customers.html')

