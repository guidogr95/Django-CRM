from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent
from .forms import AgentModelForm

class AgentListView(LoginRequiredMixin, generic.ListView):
  template_name = 'agents/agent_list.html'
  queryset = Agent.objects.all()
  context_object_name = 'agents'
  
class AgentDetailView(LoginRequiredMixin, generic.DetailView):
  template_name = 'agents/agent_detail.html'
  queryset = Agent.objects.all()
  context_object_name = 'agent'
  
class AgentCreateView(LoginRequiredMixin, generic.CreateView):
  template_name = 'agents/agent_create.html'
  form_class = AgentModelForm
  
  def get_success_url(self):
    return reverse('agents:agent_list')
    
  def form_valid(self, form):
    # save form but not commit to db
    agent = form.save(commit=False)
    agent.organisation = self.request.user.userprofile
    agent.save()
    
class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
  template_name = 'agents/agent_update.html'
  form_class = AgentModelForm
  queryset = Agent.objects.all()
  context_object_name = 'agent'
  
  def get_success_url(self):
    return reverse('agents:agent_detail', args=[self.object.pk])
    
class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
  template_name = 'agents/agent_delete.html'
  queryset = Agent.objects.all()
  
  def get_success_url(self):
    return reverse('agents:agent_list')