from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from forms.views import choice
from search import views as search_views
from post import feed, views

urlpatterns = [
    path('<slug:slug>', views.PostPageDetail.as_view(), name='PostPage_detail'),
    path('', views.NewsPageListView.as_view(), name='News_List'),

]
