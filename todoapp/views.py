from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import AddToDo

# Create your views here.

def home(request):
    return render(request,'todoapp/index.html')


def deleteitem(request, todoID):
    item = models.todolist.objects.get(pk=todoID)
    item.delete()
    return redirect('todoapp:todolist')

def todolist(request):

    if request.method == 'POST':
        addform = AddToDo(request.POST)
        try:
            if addform.is_valid():
                # todo = addform.cleaned_data['todo']
                # priority = addform.cleaned_data['priority']
                # models.todolist.objects.create(todo=todo, priority=priority)
                addform.save()
                return redirect('todoapp:todolist')
        except Exception as e:
            print(f'error {e}')
    else:
        addform = AddToDo()    
    todos = models.todolist.objects.all().order_by('-priority')
    return render(request, 'todoapp/todolist.html', context={'todos': todos, 'addform':addform})

