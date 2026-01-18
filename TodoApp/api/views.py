# from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from todo.models import Task
from .permissions import IsOwnerOnly

# Create your views here.
class TodoList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOnly]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOnly]
    queryset = Task.objects.all()
    serializer_class = TodoSerializer