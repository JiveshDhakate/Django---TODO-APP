from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Task


# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def markasComplete(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    task.is_completed=True
    task.save()
    return redirect('home')

def markasIncomplete(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    task.is_completed=False
    task.save()
    return redirect('home')

def deleteTask(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

def editTask(request,task_id):
    get_task=get_object_or_404(Task,id=task_id)
    if request.method=="POST":
        updated_task=request.POST['task']
        get_task.task=updated_task
        get_task.save()
        return redirect('home')
    else:
        context={'get_task':get_task}
        return render(request,'editTask.html',context)
    