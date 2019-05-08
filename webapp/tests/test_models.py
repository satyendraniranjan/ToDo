from django.test import TestCase
from ..models import Todo
from django.test import TestCase, Client
from django.urls import reverse
from ..serializers import toDoSerializer


client = Client()
class todoTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Todo.objects.create(
            name='todo1',State='Progress', Due_Date='2019-05-03', Text='Testing Progress')
        Todo.objects.create(
            name='todo2',State='Done', Due_Date='2019-05-04', Text='Testing Done')

    def test_todo1(self):
        todo_pros =  Todo.objects.get(State='Progress')
        todo_don =   Todo.objects.get(State='Done')
        self.assertEqual(
            todo_pros.get_data(), "todo1 Progress Due Date 2019-05-03 Text Testing Progress")
        self.assertEqual(
            todo_don.get_data(), "todo2 Done Due Date 2019-05-04 Text Testing Done")


