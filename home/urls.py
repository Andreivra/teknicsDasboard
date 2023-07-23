from django.urls import path
from home.views import Homepage



urlpatterns = [
    path('', Homepage.as_view(), name='home'),
]
