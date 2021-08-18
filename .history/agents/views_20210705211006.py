from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent

class AgentListView(LoginRequiredMixin, generic.ListView):
  template_name = 'agents/agent_list.html'
  queryset = Agent.objects.all()
  context_object_name = 'agents'