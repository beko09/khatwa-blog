from django.contrib import admin
from .models import Post
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


admin.site.register(Post, PostAdmin)

