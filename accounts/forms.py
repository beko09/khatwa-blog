from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import gettext_lazy as _




class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
            'password2':None,
        }
        error_messages = {
            'username': {
                'required': 'هذا الحقل مطلوب',
                
            }
        }



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        help_texts = {
            'first_name': None,
            'last_name':None,
            'email': None,
            'password1':None,
            'password2':None,
        }




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['job','phone_number', 'about_us', 'image']
        labels = {
            'job':_('الوظيفة'),
            'phone_number': _('رقم الهاتف '),
            'about_us': _(' نبذه عنك'),
            'image': _('الصورة'),
        }
        
