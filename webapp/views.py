from django.shortcuts import render
from .models import Todo
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from .serializers import toDoSerializer
from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.decorators import api_view

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


@api_view(['GET', 'POST'])
def get_post_todos(request):
#    get all Todos
    if request.method == 'GET':
        todo1 = Todo.objects.all()
        serializer = toDoSerializer(todo1, many=True)
        return Response(serializer.data)
    # insert a new record for a todos
    elif request.method == 'POST':
        return Response({})



