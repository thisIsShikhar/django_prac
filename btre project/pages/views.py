from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request, 'pages/about.html')

def index(request):
    return render(request, 'pages/index.html')

def shikhar(request):
    return render(request, 'pages/shikhar.html')