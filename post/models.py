from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django import forms
from django.shortcuts import render
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from rest_framework.fields import DateField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page, Orderable
from wagtailvideos.blocks import VideoChooserBlock
from django.urls import reverse
from snippets.snippets import NewsCategory


class PostListingPage(RoutablePageMixin, Page):
    template = 'postpages/postpagelisting.html'
    pass


class PostPage(Page):
    template = 'postpages/post.html'

    categories = ParentalManyToManyField(NewsCategory, blank=True)
    subtitle = models.CharField(max_length=56, blank=True, null=True)
    # slug1 = models.SlugField(null=False, unique=True, help_text='Введите текст который будет обозначать ссылку для данной публикации, к примеру название статьи',default='*')
    body = StreamField([
        ('Heading', blocks.CharBlock(max_length=128, form_classname='title')),
        ('Text', blocks.RichTextBlock(required=False)),
        ('image', ImageChooserBlock(required=False),),
        ('carousel', blocks.StreamBlock([
            ('image', ImageChooserBlock(required=False)),
            ('video', EmbedBlock(required=False)),

        ])),
        ('videodwnld', VideoChooserBlock(required=False),)
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple)
        ], heading='Категории'),

    ]

    def __str__(self):
        return "%s" % self.subtitle

    def get_absolute_url(self):
        return reverse('PostPage_detail', kwargs={'slug': self.slug})

