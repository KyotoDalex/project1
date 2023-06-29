from django import template
from snippets.snippets import NewsCategory, Menu

register = template.Library()


# Category snippets
@register.inclusion_tag('tags/categories.html', takes_context=True)
def categories(context):
    return {
        'categories': NewsCategory.objects.all(),
        "request": context['request']
    }


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)
