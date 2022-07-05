from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Task
from django.urls import reverse_lazy
# Create your views here.

class TaskListView(ListView):
    model=Task
    context_object_name = 'task'
    template_name = 'task_list.html'
class TaskCreateView(CreateView):

    model=Task
    fields = '__all__'
    template_name = 'taskcreate.html'

    success_url = reverse_lazy('tasklist')

