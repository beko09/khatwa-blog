from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post
from django.utils.translation import gettext_lazy as _





class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = ['title', 'description','image', 'content', 'draft' ,'category' , 'publish']
        labels = {
            'title': _('العنوان'),
            'description': _('الوصف المتخصر '),
            'image': _('الصورة '),
            'content': _(' الموضوع'),
            'draft': _('مسودة'),
            'category': _('القسم '),
            'publish': _('التاريخ '),
        }
        
        
