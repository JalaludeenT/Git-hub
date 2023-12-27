from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import todoform

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

class task_list_view(ListView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task1'


class task_detail_view(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task2'


class task_update_view(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task3'
    fields = ('name', 'priority', 'Date')

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk': self.object.id})
        # kwargs means keyword arguments , reverse_lazy is used to link the urls


class task_delete_view(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


def todo_home(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        Date = request.POST.get('Date', '')
        task = Task(name=name, priority=priority, Date=Date)
        task.save()
        return redirect('/')
    return render(request, 'task.html', {'task1': task1})


def todo_details(request):
    task = Task.objects.all()
    return render(request, 'details.html', {'task': task})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form = todoform(request.POST or None, request.FILES, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'Form': form, 'tasks': task})
