from django.shortcuts import render
from .models import Author
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.
def author(request):
    authors = Author.objects.all().values()
    template = loader.get_template('post.html')
    context = {
        'authors': authors
    }
    return HttpResponse(template.render(context, request))
