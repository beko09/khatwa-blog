from django.contrib import admin
from .models import Post,Category
from django.db import models
from pagedown.widgets import AdminPagedownWidget
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated', 'publish_at',)
    list_display_links = ['title','updated']
    list_filter = ('title', 'updated')
    ordering = ['publish_at']
    search_fields = ['title', 'content']
    # list_editable = ['title']
    class Meta:
        modal = Post

class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget':AdminPagedownWidget},
    }


admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ['name']
    list_filter = ('name',)
    ordering = ['name']
    search_fields = ['name']
    # list_editable = ['title']
    class Meta:
        modal = Category


admin.site.register(Category,CategoryAdmin)

