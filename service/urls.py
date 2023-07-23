from django.urls import path
from service import views

urlpatterns = [
    path('list_of_tasks/', views.ServiceTaskListView.as_view(), name='list-of-tasks'),
    path('create_task/', views.ServiceTaskCreateView.as_view(), name='create-service-task'),
    path('task_details/<int:pk>/', views.ServiceTaskDetailsView.as_view(), name='task-details'),
]
