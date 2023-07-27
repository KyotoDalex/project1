from django.core.paginator import Paginator
from django.shortcuts import render

from post.models import PostPage
from snippets.models import Author
from datetime import datetime,timedelta
def breaking_news(request):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=1)
    breaking_post = PostPage.objects.order_by('breaking_validates').filter(breaking_validates=True,pub_date__range=[start_date,end_date])[:5]
    return  {'latest_posts': breaking_post}

def last_news(request):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        last_news=PostPage.objects.order_by('-pub_date').filter(pub_date__range=[start_date,end_date])
        return {'last_news':last_news}
def all_posts(request):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        all_post = PostPage.objects.order_by('?').all().filter(pub_date__range=[start_date,end_date])
        return {'all_news': all_post}
def all_posts2(request):
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(days=7)
    all_post = PostPage.objects.order_by('?').all().filter(pub_date__range=[start_date, end_date])
    return {'all_news2': all_post}
def all_posts3(request):
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(days=7)
    all_post = PostPage.objects.order_by('?').all().filter(pub_date__range=[start_date, end_date])
    return {'all_news3': all_post}
def yamal_news(request):
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(days=7)
    yamal_post = PostPage.objects.order_by("yamal").filter(yamal=True,pub_date__range=[start_date, end_date]).order_by('-pub_date')
    return {'yamal_posts':yamal_post}
def ugra_news(request):
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(days=7)
    ugra_post = PostPage.objects.order_by('ugra').filter(ugra=True,pub_date__range=[start_date, end_date]).order_by('-pub_date')
    return {'ugra_posts':ugra_post}

def tyumen_news(request):
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(days=7)
    tyumen_post = PostPage.objects.order_by('tyumen').filter(tyumen=True,pub_date__range=[start_date, end_date]).order_by('-pub_date')
    return {'tyumen_posts':tyumen_post}

def listing(request):
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(weeks=521)
    contact_list = PostPage.objects.all().order_by('-pub_date').filter(pub_date__range=[start_date, end_date])
    paginator = Paginator(contact_list, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return {"page_obj": page_obj}

def ugra_listing(request):
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(weeks=521)
    contact_list = PostPage.objects.all().filter(ugra=True,pub_date__range=[start_date, end_date])
    paginator = Paginator(contact_list, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return {"ugra_page": page_obj}
def tyumen_listing(request):
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(weeks=521)
    contact_list = PostPage.objects.all().filter(tyumen=True,pub_date__range=[start_date, end_date])
    paginator = Paginator(contact_list, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return {"tyumen_page": page_obj}
def yamal_listing(request):
    end_date = datetime.now()
    start_date = datetime.now() - timedelta(weeks=521)
    contact_list = PostPage.objects.all().filter(yamal=True,pub_date__range=[start_date, end_date])
    paginator = Paginator(contact_list, 6)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return {"yamal_page": page_obj}
def author_check(request):
    author_ch = PostPage.objects.filter(orig_author=True).all()
    author = PostPage.objects.order_by('original_author').all()
    return {'author_check':author_ch,
            'author':author}
def random_person(request):
    person = Author.objects.order_by("?").all()
    return {'person':person}
def hmao_valid(request):
    hmao = PostPage.objects.order_by('ugra')
    return {'ugra':hmao}

def tyumen_valid(request):
    tyumen = PostPage.objects.order_by('tyumen')
    return {'tyumen':tyumen}
def yamal_valid(request):
    yamal = PostPage.objects.order_by('yamal')
    return {'yamal':yamal}
