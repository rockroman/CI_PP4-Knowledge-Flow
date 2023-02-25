from django.shortcuts import render
from django.core.exceptions import PermissionDenied

""" Error handling """


def handler404(request, exception):
    """Rendering the 404 page."""
    return render(request, '404.html', status=404)


def handler500(request):
    """Rendering the 500 page."""
    return render(request, '500.html', status=500)


def handler403(request, exception):
    """Rendering the 403 page."""
    if isinstance(exception, PermissionDenied):
        return render(request, '403.html', status=403)
    else:
        # Handle unexpected errors with a generic 500 error page
        return render(request, '500.html', status=500)
