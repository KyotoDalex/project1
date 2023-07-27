from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from django.contrib import admin
# Register your models here.
from .models import SubscribedUsers

class Subscriber(ModelAdmin):
    model = SubscribedUsers
    menu_icon = 'placeholder'
    menu_label = 'Пользователи'
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('email',)


modeladmin_register(Subscriber)
