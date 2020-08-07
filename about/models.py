from django.db import models

# Create your models here.


class Info(models.Model):
    about = models.TextField(verbose_name='المحتوي')


    def __str__(self):
        return self.about

class NewsLetterUser(models.Model):
    email = models.EmailField(verbose_name=' الايميل')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(set):
        return set.email