from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django import forms
from django.shortcuts import render
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from rest_framework.fields import DateField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.blocks import BlockQuoteBlock
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page, Orderable
from wagtailvideos.blocks import VideoChooserBlock
from django.urls import reverse

from profanity.validators import validate_is_profane
from snippets.models import BreakingNews
import datetime


class PostListingPage(RoutablePageMixin, Page):
    template = 'postpages/postpagelisting.html'
    pass

class PostPage(RoutablePageMixin, Page):
    template = 'post.html'
    breaking_validates = models.BooleanField(blank=True, null=True,
                                             help_text='Поставтьте данную галочку чтобы данная новость отображалась в разделе срочных',
                                             verbose_name='Срочная новость')
    tyumen = models.BooleanField(blank=True, null=True,
                                             help_text='Поставтьте данную галочку чтобы данная новость отображалась в разделе Тюмень',
                                             verbose_name='Новость в Тюмени')
    yamal = models.BooleanField(blank=True, null=True,
                                 help_text='Поставтьте данную галочку чтобы данная новость отображалась в разделе Тюмень',
                                 verbose_name='Новость в ЯНАО')
    ugra = models.BooleanField(blank=True, null=True,
                                 help_text='Поставтьте данную галочку чтобы данная новость отображалась в разделе Тюмень',
                                 verbose_name='Новость в ХМАО')
    pub_date = models.DateField(null=True, blank=False, default=datetime.datetime.now())
    orig_author = models.BooleanField(blank=True,null=True,help_text='Укажите есть ли наличие оригинального автора публикации',verbose_name='Проверка автора')
    body = StreamField([
        ('Heading', blocks.CharBlock(related_name='Заголовок',min_length=15, max_length=128, form_classname='title',
                                     validators=[validate_is_profane]),),
        ('Text', blocks.RichTextBlock(required=True, validators=[validate_is_profane], related_name='Текст')),
        ('image', ImageChooserBlock(required=False, related_name='Изображение')),
        ('main_image', ImageChooserBlock(required=False, related_name='Заглавное изображение')),
        ('quote', BlockQuoteBlock(related_name='Цитата')),
        ('carousel', blocks.StreamBlock([
            ('image', ImageChooserBlock(required=False)),
            ('video', EmbedBlock(required=False)),

        ], related_name='Карусель')),
        ('videodwnld', VideoChooserBlock(required=False, related_name='Видео'),),
        ('original_author', blocks.TextBlock(max_length=50, required=False,
                                             help_text='Укажите автора статьи при необходимости,в ином случае автор публикации будет выбран из  заранее оформленного списка авторов'))
    ], use_json_field=True, )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('breaking_validates')
        ], heading='Breaking News'),
        FieldPanel('pub_date'),
        MultiFieldPanel([
            FieldPanel('tyumen'),
            FieldPanel('yamal'),
            FieldPanel('ugra')
        ],heading='Категории'),
        FieldPanel('orig_author')

    ]

    def get_absolute_url(self):
        return reverse('PostPage_detail', kwargs={'slug': self.slug})

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context['post_entries'] = PostPage.objects.child_of(self).live()
    #     return context, request

    def __str__(self):
        return "%s" % self.title



