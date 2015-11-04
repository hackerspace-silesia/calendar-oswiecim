from .mixins import HasAccessMixin

def can_add_new_event(request):
    obj = HasAccessMixin()
    return {
        'can_add_event': obj.has_access(request.user, action='add')[0]
    }