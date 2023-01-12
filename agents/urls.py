from django.urls import path,include
from .views import *

app_name="agents"

urlpatterns=[
    path('',AgentsListView.as_view(),name="list_agents"),
    path('agent_create/',AgentCreateView.as_view(),name="agent_create"),
    path('agent_delete/<int:pk>',AgentDeleteView.as_view(),name="agent_delete")
]