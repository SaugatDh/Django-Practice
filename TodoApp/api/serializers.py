from rest_framework import serializers
from todo.models import Task

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model=Task
        fields = ('id','title','completed','user')
