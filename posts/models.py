from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from .utils import get_red_time
# Create your models here.


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
    # image_name, extension = filename.split(".")
    # return "post/%s/%s.%s" % (instance.id, instance.id, filename)
    return "post/%s/%s" % (instance.id, filename)


# def image_upload(instance, filename):
#     image_name, extension = filename.split(".")
#     return "job/%s.%s" % (instance.id, extension)

class Post(models.Model):
    user = models.ForeignKey(
        User, related_name='Post_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)  # unique=True
    image = models.ImageField(upload_to=upload_location, null=True, blank=True,
                              height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    read_time = models.TimeField(blank=True,null=True)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    publish_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = PostManager()


    def __str__(self):
        return self.title

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs


    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type.model


    def get_absolute_url(self):
        return reverse("posts:post_detail", kwargs={"slug": self.slug})

    def get_markdown(self):
        content = self.content
        markdown_text =  markdown(content)
        return mark_safe(markdown_text)

    class Meta:
        ordering = ["-publish_at", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title,allow_unicode=True)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
    
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    if instance.content:
        html_string = instance.get_markdown()
        read_time = get_red_time(html_string)
        instance.read_time = read_time


pre_save.connect(pre_save_post_receiver, sender=Post)
