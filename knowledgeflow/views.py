from django.shortcuts import render

""" Error handling """


def handler404(request, exception):
    """Rendering the 404 page."""
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """Rendering the 500 page."""
    return render(request, 'errors/500.html', status=500)