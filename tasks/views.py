from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "tasks": tasks,
        "form": form
    }
    return render(request, "index.html", context)


def update_task(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=tasks)

        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "update_task.html", context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("/")

    context = {
        "task": task
    }
    return render(request, "delete.html", context)
