from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultipleChooserPanel
from wagtail.api import APIField
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page, Orderable
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Введите ваше название')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('image', ImageChooserBlock(required=True)),
                ('title', blocks.CharBlock(required=True, max_length=40),),
                ('text', blocks.TextBlock(required=True, max_length=1000)),
                ('button_page', blocks.PageChooserBlock(required=False)),
                (
                    'button_url',
                    blocks.URLBlock(required=False, help_text='If button above used,this button comes first'))
            ],

        )
    )


class MainPageCarousel(Orderable):
    page = ParentalKey('MainPage', related_name='Slider')
    carousel_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        verbose_name='Слайдер'
    )
    panels = [

        FieldPanel('carousel_image')
    ]


class MainPage(Page):
    template = 'home/home_page.html'
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic", "h1", "h2"])
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
        verbose_name='Изображение'
    )
    content = StreamField([
        ('cards', CardBlock())

    ], use_json_field=True, null=True, blank=True, verbose_name='Карточки'
    )

    api_fields = [
        APIField('banner_title'),
        APIField('banner_subtitle'),
        APIField('banner_image')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle'),
        FieldPanel('banner_image'),
        MultipleChooserPanel(
            'Slider', label='Слайдер', chooser_field_name='carousel_image'

        ),

        FieldPanel('content')
    ]

    class Meta:
        verbose_name = 'Главная страница'
