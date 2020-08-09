
from django.urls import path,re_path
from . import views

app_name = 'about'

urlpatterns = [
    path('about/', views.about, name="about"),
    # path('te',views.newsletter_singup,name='newsletter_singup'),
    path('newsletter_unsubscribe/',views.newsletter_unsubscribe,name='newsletter_unsubscribe'),
    path('control_newsletter/',views.control_newsletter,name='control_newsletter'),
]
