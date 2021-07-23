from django.shortcuts import render
from .models import Tour


def tours(request):
    tour_objects = Tour.objects.all()
    return render(request, 'tours/tours.html', {'tours': tour_objects})
