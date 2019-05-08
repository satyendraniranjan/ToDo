from django.test import TestCase
from ..models import Todo


class todoTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Todo.objects.create(
            State='Progress', Due_Date='2019-05-03', Text='Testing Progress')
        Todo.objects.create(
            State='Done', Due_Date='2019-05-04', Text='Testing Done')

    def test_puppy_breed(self):
        todo_pros =  Todo.objects.get(State='Progress')
        todo_don =   Todo.objects.get(State='Done')
        self.assertEqual(
            todo_pros.get_data(), "Progress Due Date 2019-05-03 Text Testing Progress")
        self.assertEqual(
            todo_don.get_data(), "Done Due Date 2019-05-04 Text Testing Done")