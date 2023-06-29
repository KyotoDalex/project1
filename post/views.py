from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostPage
# Create your views here.

class NewsPageListView(ListView):
    model = PostPage
    context_object_name = 'News_List'
    template_name = 'postpages/postpagelisting.html'

class PostPageDetail(DetailView):
    model = PostPage
    context_object_name = 'Post'
    template_name = 'postpages/post.html'
