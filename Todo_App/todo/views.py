from django.shortcuts import render,redirect,get_object_or_404
from .models import Mytodo
from .forms import TodoForm

# Create your views here.

def alltask(request):
    tasks = Mytodo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    tasks = tasks.reverse()
    return render(request, 'todo/all_task.html',{'tasks': tasks, 'form':form})


def task_detail_page(request,pk):
    task_data = get_object_or_404(Mytodo,pk=pk)
    return render(request,'todo/task_detail.html',{'data':task_data})

def delete_task(request, pk):
    dele_task = get_object_or_404(Mytodo, id= pk)
    dele_task.delete()
    return redirect('alltask')

def update_task(request, pk):
    up_task = get_object_or_404(Mytodo, id= pk)
    updateForm = TodoForm(instance=up_task)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance = up_task)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltask')
    return render(request,'todo/updatetask.html',{'djangotodo': up_task, 'updateform': updateForm})

# def ordering(request, pk):
#     status = get_object_or_404(Mytodo, id=pk)
#     return render(request,'todo/task_detail.html',{'djangotodo': status})