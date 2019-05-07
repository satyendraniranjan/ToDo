from rest_framework import serializers
from .models import Todo

class toDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
#        fields = {'firstname','lastname'}
        fields = [
            'id',
            'State',
            'Due_Date',
            'Text',
        ]
