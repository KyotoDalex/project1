from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import PostPage
from snippets.snippets import NewsCategory


class LatestPostsFeed(Feed):
    title1 = 'Post'
    link = '/latestnews/'
    description = 'New posts'
    body = PostPage.body
    category = NewsCategory

    def items(self):
        return PostPage.objects.order_by('-last_published_at')[:5]

        def item_title(self, item):
            return item.title1

        def item_description(self, item):
            return truncatewords(item.body, 30)

        def categories(self, item):
            return item.category
