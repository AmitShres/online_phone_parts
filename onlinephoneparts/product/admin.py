from django.contrib import admin
from .models import *

# Register your models here.
class ImagesTabularinLine(admin.TabularInline):
    model = Images

class TagTabularinLine(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTabularinLine, TagTabularinLine]

admin.site.register(Images)
admin.site.register(Tag)
admin.site.register(Product,ProductAdmin)