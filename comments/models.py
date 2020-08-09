from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from markdown_deux import markdown
from django.utils.safestring import mark_safe




class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance): 
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager,self).filter(
            content_type=content_type, object_id=obj_id).filter(parent=None)
        return qs


class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name='Comment_user', on_delete=models.CASCADE,verbose_name='اسم المستخدم')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,verbose_name=' نوع الكائن')
    object_id = models.PositiveIntegerField(null=True,verbose_name='معرف الكائن')
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField(blank=True,null=True,verbose_name='المحتوي')
    publish_at = models.DateTimeField(auto_now=True,verbose_name='زمن الانشاء')
    parent = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.CASCADE,verbose_name='الردود')

    objects = CommentManager()

    class Meta:
        ordering = ["-publish_at"]


    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"id": self.id})


    def get_delete_url(self):
        return reverse("comments:comment_delete", kwargs={"id": self.id})
        
    
    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)
    

    def __str__(self):
        return self.user.username


    # function repleas
    def children(self):
        return Comment.objects.filter(parent=self)
    
    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        else:
            return True
