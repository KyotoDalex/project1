from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import PostPage, PostListingPage

# Register your models here.
class PostPageModel(ModelAdmin):
    model = PostPage
    menu_icon = 'pilcrow'
    list_display = ('title','pub_date')
    add_to_settings_menu = False
    add_to_admin_menu = True
    exclude_from_explorer = False
    menu_order = 200

modeladmin_register(PostPageModel)