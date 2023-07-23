from django.shortcuts import render
from django.views import View

# def homepage(requests):
#     return render(requests, 'home/welcome.html')


class Homepage(View):
    def get(self, request):
        return render(request, 'home/welcome.html')



