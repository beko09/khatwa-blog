
from django.urls import path,re_path
from . import views

app_name = 'about'

urlpatterns = [
    path('about-us/', views.about, name="about"),
]
