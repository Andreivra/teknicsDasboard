from django.db import models
from django.shortcuts import render

from service.models import Service


class Service1(Service):
    def get(self, request):
        return Service.objects.all()
