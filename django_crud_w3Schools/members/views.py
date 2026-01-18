from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.template import loader
from django.db.models import Q

# Create your views here.
# def members(request):
#     return HttpResponse("Hello World!")
# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())
def members(request):
    mymembers = Member.objects.all().values()
    template=loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request,slug):
    mymembers = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))
    
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    
def testing(request):
    # mymembers = Member.objects.all().values()
    # mymembers = Member.objects.values_list('firstName',flat=True) Gives column name
    # mymembers = Member.objects.filter(firstName="Saugat").values() # Used in filtering search items return specific rows
    # SELECT * FROM members WHERE firstname = 'Emil'; This is basically it.
    # mymembers = Member.objects.filter(lastName='Dhungana', id=2).values()
    # mydata = Member.objects.filter(firstName='Surabhi').values() | Member.objects.filter(firstName='Saugat').values()
    
    # Using Q same as OR using Filter . Q is better 
    # mydata = Member.objects.filter(Q(firstName='Saugat') | Q(firstName='Surabhi')).values()
    # mydata = Member.objects.filter(firstName__startswith='S').values() # SQL WHERE firstname LIKE 'S%'
    mydata = Member.objects.all().values() # can be used to sort the data
    template = loader.get_template('template.html')
    context = {
        'mymembers':mydata,
        'greeting':1,
    }
    return HttpResponse(template.render(context,request))
    
