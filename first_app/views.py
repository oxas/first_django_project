from django.http import HttpResponse
from django.template import loader

def home(request):
    return HttpResponse('First Application')


def homeHtml(request):
    template = loader.get_template('first_app/home.html')
    context = {'context':"App context",
    }
    return HttpResponse(template.render(context, request))