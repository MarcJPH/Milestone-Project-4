from django.shortcuts import render, get_object_or_404
from .models import Workouts

# Create your views here.

def workouts(request):
    """
    A view to return all workouts available.
    """
    
    workouts = Workouts.objects.all()

    context = {
        'workouts': workouts,
    }

    return render(request, 'workouts/workouts.html', context)