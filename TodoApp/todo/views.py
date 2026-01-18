from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request,'todo/home.html')

class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name = 'tasks'
    template_name='task_list.html'
    
    def get_queryset(self):
        return super(TaskList,self).get_queryset().filter(user=self.request.user)
       
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


    
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        messages.success(self.request,"The task was created successfully!")
        return super(TaskCreate,self).form_valid(form)
    
    
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self,form):
        messages.success(self.request,"The task was updated successfully!")
        return super(TaskUpdate,self).form_valid(form)
    def get_queryset(self):
        return super(TaskUpdate,self).get_queryset().filter(user=self.request.user)
    
    
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete,self).form_valid(form)

    def get_queryset(self):
        return super(TaskDelete,self).get_queryset().filter(user=self.request.user)