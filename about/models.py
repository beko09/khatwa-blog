from django.db import models
from mdeditor.fields import MDTextField
from django.utils.safestring import mark_safe
from markdown_deux import markdown
# Create your models here.


class Info(models.Model):
    title = models.CharField(max_length=150)
    about = MDTextField(verbose_name='المحتوي')


    def __str__(self):
        return self.title
    
    def get_markdown(self):
        about = self.about
        markdown_text =  markdown(about)
        return mark_safe(markdown_text)

class NewsLetterUser(models.Model):
    email = models.EmailField(verbose_name=' الايميل')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(set):
        return set.email