from django.conf import settings
from .mixins import HasAccessMixin


def can_add_new_event(request):
    obj = HasAccessMixin()
    return {
        'can_add_event': obj.has_access(request.user, action='add')[0]
    }

def google_analytics(request):
    ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
    if not settings.DEBUG and ga_prop_id:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id,
        }
    return {}
