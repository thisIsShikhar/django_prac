"""cman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import Accounts
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.http import HttpRequest,HttpResponse
from django.urls.conf import include

def home(request):
    return HttpResponse('home')

def dailyreports(request):
    return HttpResponse('dailyreports')

def monthlyreports(request):
    return HttpResponse('monthlyreports')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Accounts.urls'))
]
