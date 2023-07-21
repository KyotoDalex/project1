from django.core.paginator import Paginator
from django.shortcuts import render

from post.models import PostPage

def breaking_news(request):
        breaking_post = PostPage.objects.order_by('breaking_validates').filter(breaking_validates=True)[:5]
        return  {'latest_posts': breaking_post}

def last_news(request):
        last_news = PostPage.objects.order_by('-last_published_at')
        return {'last_news':last_news}
def all_posts(request):
        all_post = PostPage.objects.order_by('?').all()
        return {'all_news': all_post}
def all_posts2(request):
        all_post = PostPage.objects.order_by('?').all()
        return {'all_news2': all_post}
def all_posts3(request):
        all_post = PostPage.objects.order_by('?').all()
        return {'all_news3': all_post}

def yamal_news(request):
        yamal_post = PostPage.objects.order_by("yamal").filter(yamal=True).order_by('pub_date')
        return {'yamal_posts':yamal_post}
def ugra_news(request):
        ugra_post = PostPage.objects.order_by('ugra').filter(ugra=True).order_by('pub_date').prefetch_related()
        return {'ugra_posts':ugra_post}

def tyumen_news(request):
        tyumen_post = PostPage.objects.order_by('tyumen').filter(tyumen=True).order_by('pub_date')
        return {'tyumen_posts':tyumen_post}

def listing(request):
    contact_list = PostPage.objects.all().order_by('-last_published_at')
    paginator = Paginator(contact_list, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return {"page_obj": page_obj}

def ugra_listing(request):
    contact_list = PostPage.objects.all().filter(ugra=True)
    paginator = Paginator(contact_list, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return {"ugra_page": page_obj}
def tyumen_listing(request):
    contact_list = PostPage.objects.all().filter(tyumen=True)
    paginator = Paginator(contact_list, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return {"tyumen_page": page_obj}
def yamal_listing(request):
    contact_list = PostPage.objects.all().filter(yamal=True)
    paginator = Paginator(contact_list, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return {"yamal_page": page_obj}
def author_check(request):
    author = PostPage.objects.filter(orig_author=True).all()
    return {'author':author}