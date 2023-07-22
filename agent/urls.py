from django.urls import path
from agent import views

urlpatterns = [
    path('create_agent/', views.AgentCreateView.as_view(), name='create-agent'),
    path('list_of_agents/', views.AgentListView.as_view(), name='list-of-agents'),
    path('update_agent/<int:pk>/', views.AgentUpdateView.as_view(), name='update-agent'),
    path('delete_agent/<int:pk>/', views.AgentDeleteView.as_view(), name='delete-agent'),
    path('agent_details/<int:pk>/', views.AgentDetailsView.as_view(), name='agent-details'),
]
