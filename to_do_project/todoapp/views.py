
import mysql.connector
conn= mysql.connector.connect(host='localhost',username='root',password='',database='todo_db')
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task


def index(request):
    tasks= Task.objects.all()
    return render(request,'index.html',{'tasks':tasks})

def add_task(request):
    if request.method=="POST":
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(task=task_text)
    return redirect('index')

def complete_task(request,task_id):
    task=Task.objects.get(id=task_id)
    task.status = True
    task.save()
    return redirect('index')

def delete_task(request,task_id):
    
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')


    
