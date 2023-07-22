from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from agent.models import Agent
from agent.forms import AgentForm, AgentUpdateForm


class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'agent/create_agent.html'
    model = Agent
    form_class = AgentForm
    success_url = reverse_lazy('list-of-agents')
    success_message = "Agentul {first_name} {last_name} a fost creat cu success"
    permission_required = 'agent.add_agent'

    def form_valid(self, form):
        if form.is_valid():
            new_agent = form.save(commit=False)
            new_agent.first_name = new_agent.first_name.title()
            new_agent.last_name = new_agent.last_name.title()
            new_agent.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message.format(first_name=self.object.first_name, last_name=self.object.last_name)


class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agent/list_of_agents.html'
    model = Agent
    context_object_name = 'all_agents'
    permission_required = 'agent.view_list_of_agents'


class AgentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'agent/update_agent.html'
    model = Agent
    form_class = AgentUpdateForm
    success_url = reverse_lazy('list-of-agents')
    success_message = "Agentul %(first_name_field)s  %(last_name_field)s a fost actualizat cu success"
    permission_required = 'agent.change_agent'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name_field=self.object.first_name,
            last_name_field=self.object.last_name,

        )


class AgentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'agent/delete_agent.html'
    model = Agent
    success_url = reverse_lazy('list-of-agents')
    success_message = "Agentul %(first_name_field)s  %(last_name_field)s a fost sters cu success"
    permission_required = 'agent.delete_agent'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name_field=self.object.first_name,
            last_name_field=self.object.last_name,

        )


class AgentDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'agent/agent_details.html'
    model = Agent
    success_url = reverse_lazy('list-of-agents')
    permission_required = 'agent.view_agent'
