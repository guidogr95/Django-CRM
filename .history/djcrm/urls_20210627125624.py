from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add custom paths
    path('leads/', include('leads.urls', namespace="leads", app_name="leads"))
]
