import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Todo
from ..serializers import toDoSerializer


# initialize the APIClient app
client = Client()

class GetAllTodoTest(TestCase):
    """ Test module for GET all todo API """

    def setUp(self):
        Todo.objects.create(
            State='Progress', Due_Date='2019-05-03', Text='Testing Progress')
        Todo.objects.create(
            State='Done', Due_Date='2019-05-04', Text='Testing Done')

    def test_get_all_todo(self):
        # get API response
        response = client.get(reverse('get_post_todos'))
        # get data from db
        todo1 = Todo.objects.all()
        serializer = toDoSerializer(todo1, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)