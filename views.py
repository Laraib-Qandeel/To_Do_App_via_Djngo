from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm 

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')

def completeTask(request, pk):
    task = Task.objects.get(id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('/')

def home(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'home.html', {'tasks': tasks, 'form': form}) 

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.title = request.POST['title']  # update field
        task.save()                          # save changes
        return redirect('task_list')

    return render(request, 'update_task.html', {'task': task})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect('home')

    return render(request, 'register.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_view(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')