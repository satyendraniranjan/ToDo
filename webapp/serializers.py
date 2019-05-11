from rest_framework import serializers
from .models import Todo


# for multiple record update, create and delele.
class todoListSerializer(serializers.ListSerializer):

    class Meta:
        model = Todo
        fields = (
            'id',
            'name',
            'State',
            'Due_Date',
            'Text',
        )


class toDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        list_serializer_class = todoListSerializer
#        fields = {'firstname','lastname'}
        fields = [
            'id',
            'name',
            'State',
            'Due_Date',
            'Text',
        ]



