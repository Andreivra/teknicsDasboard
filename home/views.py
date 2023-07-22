from django.shortcuts import render
from django.views.generic import ListView
from service.models import Service

def homepage(requests):
    return render(requests, 'home/welcome.html')


class DashServiceTaskListView(ListView):
    template_name = 'home/welcome.html'
    model = Service
    context_object_name = 'all_tasks'
    # permission_required = 'task.view_task_list'
