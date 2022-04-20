from django.http import HttpResponse


def index(request):
    """Index."""
    return HttpResponse('У меня получилось!')


def second_page(request):
    """Second page."""
    return HttpResponse('А это вторая страница')
