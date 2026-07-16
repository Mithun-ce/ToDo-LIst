from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskHistory

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
            TaskHistory.objects.create(task_title=title, action='added')
        return redirect('task_list')
    return render(request, 'task_form.html')

def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    TaskHistory.objects.create(
        task_title=task.title,
        action='completed' if task.completed else 'uncompleted'
    )
    return redirect('task_list')

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    TaskHistory.objects.create(task_title=task.title, action='deleted')
    task.delete()
    return redirect('task_list')

def task_history(request):
    history = TaskHistory.objects.all()
    return render(request, 'task_history.html', {'history': history})