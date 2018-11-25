from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'today': datetime.now(),
        'app_name': "Super Todos",
    }
    return render(request, 'todo/index.html', context=context)

def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/todo_detail.html', context=context)

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Created Todos Successfully.')
            return redirect('index')
        return render(request, 'todo/create_todo.html', {'form': form})
    return render(request, 'todo/create_todo.html', {'form': TodoForm()})

def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Todos Successfully.')
            return redirect('index')
        return render(request, 'todo/create_todo.html', {'form': form})
    return render(request, 'todo/create_todo.html', {'form': TodoForm(instance=todo)})
  

