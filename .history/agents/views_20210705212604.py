from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent

class AgentListView(LoginRequiredMixin, generic.ListView):
  template_name = 'agents/agent_list.html'
  queryset = Agent.objects.all()
  context_object_name = 'agents'
  
class AgentCreateView(LoginRequiredMixin, generic.CreateView):
  template_name = 'agents/agent_create.html'
  form_class = None
  
  def get_success_url(self):
      return reverse('agents:agent_list')