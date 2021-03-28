
from rest_framework import serializers
# from rest_framework import Employee
from . models import employees

class employeeSerializers(serializers.ModelSerializer):

    class Meta:
        model= employees
    fields ='__All__' 