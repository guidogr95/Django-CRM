from django.urls import path
from .views import (
  AssignAgentView,
  LeadListView,
  LeadDetailView,
  LeadCreateView,
  LeadUpdateView,
  LeadDeleteView,
  CategoryListView
)

app_name = "leads"

urlpatterns = [
  path('', LeadListView.as_view(), name='lead_list'),
  path('create/', LeadCreateView.as_view(), name='lead_create'),
  path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign_agent'),
  path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
  path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
  path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
  path('categories/', CategoryListView.as_view(), name='category_list')
]