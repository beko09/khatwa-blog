from django.db import models

# Create your models here.


class Info(models.Model):
    about = models.TextField()


    def __str__(self):
        return self.about