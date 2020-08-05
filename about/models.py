from django.db import models

# Create your models here.


class Info(models.Model):
    description = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    about = models.TextField()


    def __str__(self):
        return self.email