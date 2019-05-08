from django.db import models
from django.utils import timezone


class Todo(models.Model):


    CHOICES1 = (
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),

    )

    State = models.CharField(max_length=255, choices=CHOICES1,null=True, blank=True)
    Due_Date = models.DateField(default=timezone.now)
    Text = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255, default='todo')



    def get_data(self):
        return self.name +' '+ self.State + ' Due Date ' + str(self.Due_Date) + ' Text ' + self.Text

    def __repr__(self):
        return self.name + ' is added.'
