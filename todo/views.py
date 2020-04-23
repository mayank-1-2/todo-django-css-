from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoitem
# Create your views here.

def index(request):
    item=todoitem.objects.all()
    return render(request,'todo/todo.html',{'todo_item':item})

def addtodo(request):
    new_item=request.POST.get("title")
    new_item1=request.POST.get("content")
    print(new_item,"jdhjhu")
    do=todoitem(title=new_item,content=new_item1)
    do.save()
    return HttpResponseRedirect('/index/')

def deltodo(request,todo_id):
     dele=todoitem.objects.get(id=todo_id)
     dele.delete()
     return HttpResponseRedirect('/index/')


