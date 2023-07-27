
from django.urls import include, path,re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

import home
from newsletter.views import  validate_email, SubView
from search import views as search_views
from post import feed,views
from .views import sass_page_handler, login,yanao,hmao,tyumen


urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    re_path(r'^validate/', validate_email, name='validate_email'),
    re_path(r'^newsletter/', SubView.as_view(), name='subscribe1'),
    path('feed/rss', feed.LatestPostsFeed(),name='post_feed'),
    path('',sass_page_handler),
    path('accounts/login/', login),
    path('<slug:slug>', views.PostPageDetail.as_view(), name='PostPage_detail'),
    path('news/', views.last_news),
    path('yanao/',yanao),
    path('hmao/',hmao),
    path('tyumen/',tyumen)


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
