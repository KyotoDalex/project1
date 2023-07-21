from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from wagtail.contrib.routable_page.models import route
from django.template import loader
from .models import PostPage
from django.views.generic import CreateView


# Create your views here.

# class NewsPageListView(ListView):
#     model = PostPage
#     context_object_name = 'News_List'
#     template_name = 'lastnews.html'
#     paginate_by = 6

def last_news(request):
    return render(request,'lastnews.html')

class PostPageDetail(DetailView):
    model = PostPage
    context_object_name = 'Post'
    template_name = 'post.html'


