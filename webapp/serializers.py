from rest_framework import serializers
from .models import Todo

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
#        fields = {'firstname','lastname'}
        fields = '__all__'
