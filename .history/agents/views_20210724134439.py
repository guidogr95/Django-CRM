import random
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin

class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
  template_name = 'agents/agent_list.html'
  context_object_name = 'agents'
  def get_queryset(self):
    organisation = self.request.user.userprofile
    return Agent.objects.filter(organisation=organisation)
  
class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
  template_name = 'agents/agent_detail.html'
  context_object_name = 'agent'
  def get_queryset(self):
    organisation = self.request.user.userprofile
    return Agent.objects.filter(organisation=organisation)
  
class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
  template_name = 'agents/agent_create.html'
  form_class = AgentModelForm
  
  def get_success_url(self):
    return reverse('agents:agent_list')
    
  def form_valid(self, form):
    # save form but not commit to db
    user = form.save(commit=False)
    user.is_agent = True
    user.is_organisor = False
    # set password by hashing it
    user.set_password(f'{random.randint(0, 1000000)}')
    user.save()
    Agent.objects.create(
      user = user,
      organisation=self.request.user.userprofile
    )
    send_mail(
      subject='You are invited to be an agent.',
      message='You were added as an agent to DJCRM. Please come login to start working.',
      from_email='admin@test.com',
      recipient_list=[user.email]
    )
    return super(AgentCreateView, self).form_valid(form)
  
class LeadUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
  template_name = 'leads/lead_update.html'
  form_class = LeadModelForm
  
  @get_role_based_leads
  def get_queryset(self):
    return self.queryset
  
  def get_success_url(self):
    return reverse('leads:lead_detail', args=[self.object.pk])
    
class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
  template_name = 'agents/agent_update.html'
  form_class = AgentModelForm
  queryset = Agent.objects.all()
  
  def get_success_url(self):
    return reverse('agents:agent_detail', args=[self.object.pk])
    
class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
  template_name = 'agents/agent_delete.html'
  
  def get_success_url(self):
    return reverse('agents:agent_list')
  
  def get_queryset(self):
    organisation = self.request.user.userprofile
    return Agent.objects.filter(organisation=organisation)