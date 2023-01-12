from django.shortcuts import render,reverse
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,DeleteView
from leads.models import *
from .mixins import OrganizerRequiredMixin

# Create your views here.

class AgentsListView(LoginRequiredMixin,OrganizerRequiredMixin,ListView):
    template_name="agents/list_agents.html"
    context_object_name="agents"

    def get_queryset(self):
        organizer=self.request.user.organizer
        queryset=Agent.objects.filter(organizer=organizer)
        return queryset

class AgentCreateView(LoginRequiredMixin,CreateView):
    template_name="agents/agent_create.html"
    form_class=AgentForm

    def get_success_url(self):
        return reverse('agents:list_agents')

    def form_valid(self,form):
        agent=form.save(commit=False)
        agent.organizer=self.request.user.organizer
        agent.save()
        return super().form_valid(form)

class AgentDeleteView(LoginRequiredMixin,DeleteView):
    template_name="agents/agent_delete.html"


    def get_success_url(self):
        return reverse('agents:list_agents')
    
    def get_queryset(self):
        organizer=self.request.user.organizer
        queryset=Agent.objects.filter(organizer=organizer)
        return queryset
