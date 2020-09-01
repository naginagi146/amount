from django.contrib import admin
from .models import Item, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 5


class ItemAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Item, ItemAdmin)
# from .forms import *

# class Postadmin(admin.ModelAdmin):
#     form = PostCreateForm

# Register your models here.
