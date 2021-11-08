from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


# def response_error_handler(request, exception=None):
#     context = {}
#     return render(request, '403.html', context, status=403 )


def permission_denied_view(request, exception=None):
    # raise PermissionDenied
    context = {}
    return render(request, '403.html', context, status=403)


def page_not_found_view(request, exception=None, template_name="404.html"):
    context = {}
    return render(request, '404.html', context, status=404)
