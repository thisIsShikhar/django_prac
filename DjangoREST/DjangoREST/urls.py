
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from REST_API import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employees/',views.employeelist.as_view())
]
