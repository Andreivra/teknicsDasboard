from django.urls import path
from home.views import homepage


urlpatterns = [
    path('', homepage, name='home'),
    path('dasboard_task_view/', ServiceTaskListView.as_view(), name='dash-task-view')
]
