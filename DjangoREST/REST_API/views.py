from django.shortcuts import render

from django.http import HttpResponse, response
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeeSerializers


class employeelist(APIView):
    def get(self,request):
        employee1=employees.objects.all()
        serializer= employeeSerializers(employee1,many=True)
        return Response(serializer.data)

    def post(self):
        pass
