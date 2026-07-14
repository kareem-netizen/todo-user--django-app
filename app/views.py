from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import Task
from .forms import TaskForm




#----------Register----------
from django.contrib.auth.forms import UserCreationForm

def register_view(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("task_list")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})




#----------Login----------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("task_list")

    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})




#----------logout----------
from django.contrib.auth.decorators import login_required

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")




#
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    completed_count = Task.objects.filter(
        user=request.user,
        completed=True
    ).count()

    return render(request, "task_list.html", {
        "tasks": tasks,
        "completed_count": completed_count
    })




#
@login_required
def create_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user

            task.save()

            return redirect("task_list")

    else:
        form = TaskForm()

    return render(request, "create_task.html", {"form": form})




#
@login_required
def update_task(request, id):

    task = Task.objects.get(id=id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()

            return redirect("task_list")

    else:
        form = TaskForm(instance=task)

    return render(request, "update_task.html", {"form": form})




#
@login_required
def delete_task(request, id):

    task = Task.objects.get(id=id, user=request.user)

    if request.method == "POST":
        task.delete()

        return redirect("task_list")

    return render(request, "delete_task.html", {"task": task})