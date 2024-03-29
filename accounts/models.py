from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='معرف الكائن')
    phone_number = models.CharField(max_length=15,verbose_name=' رقم الهاتف')
    image = models.ImageField(upload_to="profile/",
                              default="profile/default.jpg",verbose_name=' الصورة')
    about_us = models.TextField(max_length=200, verbose_name=' نبذه عنك')
    job = models.CharField(max_length=100, verbose_name='الوظيفة', blank=True,null=True)
    featured_member = models.BooleanField(default=False, verbose_name='عضو مميز')
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def get_profile_url(self):
        return reverse("accounts:profile", kwargs={"user": self.user})

   

    def __str__(self):
        return str(self.user)


