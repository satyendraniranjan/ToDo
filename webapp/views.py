from django.shortcuts import render
from .models import Todo
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from .serializers import toDoSerializer, todoListSerializer
from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from datetime import datetime

# Create your views here.





@api_view(['GET', 'POST'])
def get_post_todos(request):
#    get all Todos
    if request.method == 'GET':
        todo1 = Todo.objects.all()
        serializer = toDoSerializer(todo1, many=True)
        return Response(serializer.data)
    # insert a new record for a todos

    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'Due_Date': request.data.get('Due_Date'),
            'State': request.data.get('State'),
            'Text': request.data.get('Text')
        }
        """serializer1 = todoListSerializer(data=data, many=True)
        if serializer1:
            if serializer1.is_valid():
                serializer1.save()
                return Response(serializer1.data, status=status.HTTP_201_CREATED)
            return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)"""

        serializer = toDoSerializer(data=data)
        if serializer:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'UPDATE', 'DELETE'])
def get_delete_update_todos(request, pk):
    try:
        todo1 = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single todo
    if request.method == 'GET':
        serializer = toDoSerializer(todo1)
        return Response(serializer.data)

        # update details of a single puppy

    if request.method == 'PUT':
        serializer = toDoSerializer(todo1, data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single todos
    elif request.method == 'DELETE':
        todo1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
class toDoList(APIView):

    def get(self, request):
        todo1 = Todo.objects.all()
        serializer = toDoSerializer(todo1, many=True)
        return Response(serializer.data)








class toDoRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field            = 'pk'
    serializer_class        = toDoSerializer

    def get_queryset(self):
        return Todo.objects.all() """

