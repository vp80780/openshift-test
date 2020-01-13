from django.core.exceptions import PermissionDenied

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return PermissionDenied
        return wrap
    return decorator