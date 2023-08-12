from django.shortcuts import render
from django.views.generic.base import View

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, 'home.html')
        
class Projects(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, 'projects.html')
        
class About(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, 'about.html')