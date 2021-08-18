from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView

app_name = 'agents'

urlpatterns = [
  path('', AgentListView.as_view(), name='agent_list'),
  path('create/', AgentCreateView.as_view(), name='agent_create'),
  # path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
  # path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
  path('<int:pk>/', AgentDetailView.as_view(), name='agent_detail')
]
