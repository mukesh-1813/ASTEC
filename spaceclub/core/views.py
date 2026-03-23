from django.shortcuts import render
from magazines.models import Magazine
from events.models import Event

def home(request):
    featured_magazines = Magazine.objects.all()[:3]
    upcoming_events = Event.objects.filter(event_status='active')[:3]
    return render(request, 'core/home.html', {
        'featured_magazines': featured_magazines,
        'upcoming_events': upcoming_events
    })

def about(request):
    return render(request, 'core/about.html')
