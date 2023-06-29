from django.db import models
from django import forms
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Page



class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)


class SubscribePage(Page):

    template = "subscribe.html"
