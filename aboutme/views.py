from django.shortcuts import render
from .models import Person

def aboutme(request):
    person = Person.objects.get(pk=0)
    context = {'person': person}
    return render(request, 'aboutme.html', context)

