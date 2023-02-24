from django.shortcuts import render

""" Error handling """


def handler404(request, exception):
    """Render the 404 page."""
    return render(request, 'errors/404.html', status=404)


