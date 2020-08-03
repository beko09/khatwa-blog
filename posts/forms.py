from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'draft', 'publish']
        labels = {
            'title': _('العنوان '),
            'image': _('الصورة '),
            'content': _(' الموضوع'),
            'draft': _('مسودة'),
            'publish': _('التاريخ '),
        }
