from django.shortcuts import render
from .models import Todo
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from .serializers import toDoSerializer
from django.db.models import Q
from rest_framework import generics, mixins


# Create your views here.

class toDoList(APIView):

    def get(self, request):
        todo1 = Todo.objects.all()
        serializer = toDoSerializer(todo1, many=True)
        return Response(serializer.data)




class toDoRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field            = 'pk'
    serializer_class        = toDoSerializer

    def get_queryset(self):
        return Todo.objects.all()



