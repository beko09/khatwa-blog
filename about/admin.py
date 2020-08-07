from django.contrib import admin
# from pagedown.widgets import AdminPagedownWidget
# from django.db import models
# Register your models here.
from .models import Info,NewsLetterUser

class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_added']
    search_fields = ['email']

admin.site.register(NewsLetterUser,NewsLetterAdmin)
admin.site.register(Info)