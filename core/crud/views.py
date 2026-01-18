from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from .models import Item
# Create your views here.
def crud(request):
    return HttpResponse("Hello")

def create_item(request):
    if request.method == "POST":
        name = request.POST.get('task_name')
        desc = request.POST.get('description')
        
        Item.objects.create(
            user = request.user,
            task_name = name,
            description = desc
        )
        
        return redirect('/home/')
    return redirect('/home')


def delete_item(request,id):
    item = get_object_or_404(Item,id=id,user=request.user)
    item.delete()
    return redirect('/home/')

def edit_item(request,id):
    pass
    item = get_object_or_404(Item,id=id,user=request.user)
    
    if request.method == "POST":
        item.task_name = request.POST.get('task_name')
        item.description = request.POST.get('description')
        
        if request.POST.get('is_completed') == 'on':
            item.is_completed = True
        else:
            item.is_completed=False
        
        item.save()
        return redirect('/home') 
        
        
        
    return render(request,'edit.html',{'item':item})

