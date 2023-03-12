# views.py

from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def handler404(request, exception):
    return render(request, '404.html', status=404)