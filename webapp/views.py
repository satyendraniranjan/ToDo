from django.shortcuts import render
from .models import employees
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from .serializers import employeesSerializer

# Create your views here.

class employeeList(APIView):

    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass



