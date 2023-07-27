import wagtail.images
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
    parent_page_types = [PostListingPage]
    breaking_validates = models.BooleanField(blank=True,
                                             help_text='Поставтьте данную галочку чтобы данная новость отображалась в разделе срочных',
                                             verbose_name='Срочная новость',default=True)
    tyumen = models.BooleanField(blank=False, help_text='Поставтьте данную галочку чтобы данная новость отображалась в разделе Тюмень', verbose_name='Новость в Тюмени',)
    yamal = models.BooleanField(blank=False, help_text='Поставтьте данную галочку чтобы данная новость отображалась в разделе ЯНАО', verbose_name='Новость в ЯНАО',)
    ugra = models.BooleanField(blank=False,help_text='Поставтьте данную галочку чтобы данная новость отображалась в разделе ХМАО',  verbose_name='Новость в ХМАО',)
    original_author= models.TextField(max_length=50,default='',blank=True,verbose_name='Автор')
    pub_date = models.DateTimeField(null=True, blank=False, default=datetime.datetime.now(),verbose_name='Дата публикации')
    orig_author = models.BooleanField(blank=True,verbose_name='Проверка автора',default=False)

    body = StreamField([
        ('main_text',blocks.RichTextBlock(validators=[validate_is_profane],label='Основной текст',help_text='Данный блок выводиться на главную страницу',max_length=512)),
        ('Text', blocks.RichTextBlock(required=True, validators=[validate_is_profane], label='Дополнительный текст')),
        ('image', ImageChooserBlock(required=False, label='Дополнительное изображение')),
        ('main_image', ImageChooserBlock(required=False, label='Основное изображение',)),
        ('quote', BlockQuoteBlock(label='Цитата')),
        ('carousel', blocks.StreamBlock([
            ('image', ImageChooserBlock(required=False,label='Изображение')),
            ('youtube', blocks.URLBlock()),
            ('rutube', blocks.URLBlock()),

        ], label='Карусель')),
        ('videodwnld', VideoChooserBlock(required=False, label='Загруженное видео'),),
        ('video',blocks.URLBlock(label='Ссылка на видео'))

    ], use_json_field=True,verbose_name='Тело публикации')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('breaking_validates')
        ], heading='Breaking News',classname="collapsible collapsed"),

        MultiFieldPanel([
            FieldPanel('tyumen'),
            FieldPanel('yamal'),
            FieldPanel('ugra')
        ],heading='Категории',classname="collapsible collapsed",),
        MultiFieldPanel([
            FieldPanel('orig_author'),
            FieldPanel('original_author')
        ],heading='Оригинальный автор',help_text='Укажите автора статьи при необходимости,в ином случае автор публикации будет выбран из  заранее оформленного списка авторов',classname="collapsible collapsed"),
        FieldPanel('pub_date'),

    ]

    def get_absolute_url(self):
        return reverse('PostPage_detail', kwargs={'slug': self.slug})

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context['post_entries'] = PostPage.objects.child_of(self).live()
    #     return context, request

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name='Публикация'
        verbose_name_plural = 'Публикации'



