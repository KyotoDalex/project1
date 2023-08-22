# from django.db import models
# from django import forms
# from modelcluster.fields import ParentalKey
# from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
# from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
# from wagtail.fields import RichTextField
# from wagtail.models import Page
# from wagtailcaptcha.models import WagtailCaptchaEmailForm
#
#
# class SubscribedUser(models.Model):
#     email = models.CharField(unique=True, max_length=50)
#     # name = models.CharField(max_length=50)
#     # status = models.CharField(max_length=64, null=True, blank=True)
#     # created_date = models.DateTimeField(null=True, blank=True)
#
#
#     class Meta:
#         verbose_name = 'Подписчика'
#         verbose_name_plural = 'Подписчики'
#
# class FormField(AbstractFormField):
#     page = ParentalKey(
#         'ContactPage',
#         on_delete=models.CASCADE,
#         related_name='form_fields'
#     )
#
#
# class ContactPage(WagtailCaptchaEmailForm):
#     from_adress = models.URLField(max_length=150, blank=True, null=True)
#     to_adress = models.URLField(max_length=150, blank=True, null=True)
#     subject = models.CharField(max_length=100)
#     intro = RichTextField(blank=True)
#     thx_text = RichTextField(blank=True)
#     template = 'contact/contact_page.html'
#
#     content_panels = AbstractEmailForm.content_panels + [
#         FieldPanel('intro'),
#         InlinePanel('form_fields', label='Form Fields'),
#         FieldPanel('thx_text'),
#         MultiFieldPanel([
#             FieldRowPanel([
#                 FieldPanel('from_adress', classname='col6',
#                            help_text='Оставтье это поле пустым. Пользователь при обращении укажет свой адрес почты самостоятельно.'),
#                 FieldPanel('to_adress', classname='col6',
#                            help_text='Введите email на который будет отправлено обращение, для того чтобы ввести список перечисляйте через запятую.')
#             ]),
#             FieldPanel('subject'),
#         ], heading='Email Settings')
#     ]
