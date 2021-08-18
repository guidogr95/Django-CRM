from django.urls import path
from .views import (
  lead_list, lead_detail, lead_create, lead_update, lead_delete, LeadListView, LeadDetailView
  )

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('create/', lead_create, name='lead_create'),
    path('<int:pk>/delete/', LeadDetailView.as_view(), name='lead_delete'),
    path('<int:pk>/update/', lead_update, name='lead_update'),
    path('<int:pk>/', lead_detail, name='lead_detail')
]
