from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from service.forms import TaskForm, TaskUpdateForm
from service.models import Service
from agent.models import Agent
# from service.filters import TaskFilters


class ServiceTaskCreateView(SuccessMessageMixin, CreateView):
    template_name = 'service/create_service_task.html'
    model = Service
    form_class = TaskForm
    success_url = reverse_lazy('list-of-tasks')
    success_message = "Task-ul companiei {company_name} a fost creat cu success"
    permission_required = 'task.add_task'

    def form_valid(self, form):
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.company_name = new_task.company_name.title()
            new_task.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message.format(company_name=self.object.company_name)


class ServiceTaskListView(ListView):
    template_name = 'service/list_of_tasks.html'
    model = Service
    context_object_name = 'all_tasks'
    permission_required = 'task.view_task_list'

    def get_queryset(self):
        return Service.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        now = datetime.now()
        data['current_date_time'] = now
        agent = Agent.objects.all()
        data['get_all_agents'] = agent
        tasks = Service.objects.filter(active=True)
       #  my_filter = TaskFilters(self.request.GET, queryset=tasks)
       #  tasks = my_filter.qs
       #  data['all_tasks'] = tasks
       #  data['form_filters'] = my_filter.form
        return data


class ServiceTaskDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'service/task_details.html'
    model = Service
    success_url = reverse_lazy('list-of-tasks')
    permission_required = 'task.view_task'
