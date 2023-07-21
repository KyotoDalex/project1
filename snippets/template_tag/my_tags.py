from django import template
from snippets.models import AuthorChooser, Author, Menu, BreakingNews
from profanity.extras import ProfanityFilter

register = template.Library()


# breaking snippets
@register.inclusion_tag('tags/categories.html', takes_context=True)
def categories(context):
    return {
        'categories': BreakingNews.objects.all(),
        "request": context['request']
    }


@register.simple_tag()
def get_menu(slug):
    return Menu.objects.get(slug=slug)


pf = ProfanityFilter()


@register.filter()
def censor(value):
    return pf.censor(value)


@register.filter()
def is_profane(value):
    return pf.is_profane(value)


@register.simple_tag()
def get_author(slug):
    return AuthorChooser.objects.get(slug=slug)


@register.simple_tag()
def get_sign(person):
    return Author.objects.get(person=person)

@register.filter()
def upfirstletter(value):
    first = value[0] if len(value) > 0 else ''
    remaining = value[1:] if len(value) > 1 else ''
    return first.upper() + remaining