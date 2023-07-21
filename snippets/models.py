from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import InlinePanel, FieldPanel, MultiFieldPanel, PageChooserPanel

from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet
from django_extensions.db.fields import AutoSlugField

from wagtail.admin.mail import send_mail
from wagtail.contrib.forms.models import AbstractEmailForm
import datetime


class StoryManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            expiration_time__gt=datetime.datetime.now()
        )


@register_snippet
class Advert(models.Model):
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255, help_text='Введите текст рекламы')
    image = models.ImageField(null=True, blank=True)
    publish_date = models.DateTimeField(default=datetime.datetime.now,editable=True)
    expiration_time = models.DateTimeField(db_index=True, default=datetime.datetime.now, editable=True)
    panels = [
        FieldPanel('url'),
        FieldPanel('text'),
        FieldPanel('image'),
        FieldPanel('expiration_time'),
        FieldPanel('publish_date')
    ]
    objects = StoryManager()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклама'


class Author(Orderable):
    page = ParentalKey('AuthorChooser', related_name='Author', null=True)
    person = models.TextField(max_length=255, blank=True, help_text='Введите ФИО автора', null=True)
    panels = [
        FieldPanel('person')
    ]

    def __str__(self):
        return self.person


@register_snippet
class AuthorChooser(ClusterableModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', editable=True)
    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug')
        ], heading='Author'),
        InlinePanel('Author', label='Авторы'),

    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class MenuItem(Orderable):
    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    link_url = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey('Menu', related_name='menu_items')

    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        PageChooserPanel('link_page'),
        FieldPanel('open_in_new_tab')
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return "#"

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return "Missing Title"


@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', editable=True)
    disclaimer_text = models.TextField(max_length=400, editable=True, help_text='Основная подпись страниц', null='True')
    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
            FieldPanel('disclaimer_text')
        ], heading='Menu'),
        InlinePanel('menu_items', label='Menu Item')
    ]

    def __str__(self):
        return self.title



@register_snippet
class BreakingNews(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    cheked = models.BooleanField
    panels = [
        FieldPanel('title')
    ]

    class Meta:
        verbose_name='Breaking post'
        verbose_name_plural='Breaking posts'
    def __str__(self):
       return self.title
