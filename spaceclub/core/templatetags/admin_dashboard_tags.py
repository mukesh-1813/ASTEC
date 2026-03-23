from django import template
from magazines.models import Magazine
from events.models import Event, EventRegistration
from core.models import Contribution

register = template.Library()

@register.simple_tag
def get_dashboard_stats():
    return {
        'magazines_count': Magazine.objects.count(),
        'events_count': Event.objects.count(),
        'registrations_count': EventRegistration.objects.count(),
        'contributions_count': Contribution.objects.count(),
    }
