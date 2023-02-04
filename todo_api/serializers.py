from rest_framework import serializers

from .models import ToDoList

class ToDoListSerializer(serializers.ModelSerializer):
    task = serializers.CharField(required=True)
    class Meta:
        model = ToDoList
        fields = ['id','task','is_completed']