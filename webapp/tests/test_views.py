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
        self.todo1 =Todo.objects.create(
            name='todo1', State='Progress', Due_Date='2019-05-03', Text='Testing Progress')
        self.todo2 = Todo.objects.create(
            name='todo2',State='Done', Due_Date='2019-05-04', Text='Testing Done')
        self.todo3 = Todo.objects.create(
            name='todo3',State='', Due_Date='2019-05-04', Text='Testing Done')
        self.todo4 = Todo.objects.create(
            name='todo4',State='Done', Due_Date='2019-05-04', Text='Testing Done')

    def test_get_all_todo(self):
        # get API response
        response = client.get(reverse('get_post_todos'))
        # get data from db
        todo1 = Todo.objects.all()
        serializer = toDoSerializer(todo1, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_valid_single_todo(self):
        response = client.get(
        reverse('get_delete_update_todos', kwargs={'pk': self.todo3.pk}))
        todo1 = Todo.objects.get(pk=self.todo3.pk)
        serializer = toDoSerializer(todo1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_todo(self):
        response = client.get(
            reverse('get_delete_update_todos', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewTodoTest(TestCase):
    """ Test module for inserting a new todo """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'Status': 'Progress',
            'Due_Date': '2019-05-03',
            'Text': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'Status': 'Progress',
            'Due_Date': '2019-05-05',
            'Text': 'black'
        }

    def test_create_valid_todo(self):
        response = client.post(
            reverse('get_post_todos'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_todo(self):
        response = client.post(
            reverse('get_post_todos'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleTodoTest(TestCase):
    """ Test module for updating an existing puppy record """

    def setUp(self):
        self.casper = Todo.objects.create(
            name='casper', State='Done', Due_Date='2019-05-04', Text='Testing Done')
        self.muff = Todo.objects.create(
            name='muff', State='Done', Due_Date='2019-05-04', Text='Testing Done')
        self.valid_payload = {
            'name': 'muff',
            'State': 'In Progress',
            'Due_Date': '2019-05-03',
            'Text': 'White123'
        }
        self.invalid_payload = {
            'name': '',
            'State': '',
            'Due_Date': '',
            'Text': 'White123'
        }

    def test_valid_update_todo(self):
        response = client.put(
            reverse('get_delete_update_todos', kwargs={'pk': self.casper.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_todo(self):
        response = client.put(
            reverse('get_delete_update_todos', kwargs={'pk': self.casper.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleToDoTest(TestCase):
    """ Test module for deleting an existing puppy record """

    def setUp(self):
        self.casper = Todo.objects.create(
            name='casper', State='Done', Due_Date='2019-05-04', Text='Testing Done' )
        self.muffin = Todo.objects.create(
            name='muff', State='Done', Due_Date='2019-05-04', Text='Testing Done')

    def test_valid_delete_todo(self):
        response = client.delete(
            reverse('get_delete_update_todos', kwargs={'pk': self.muffin.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_todo(self):
        response = client.delete(
            reverse('get_delete_update_todos', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)