from django.urls import path,re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('profile/<str:username>/', views.profile, name="profile"),
    # re_path(r'^profile/(?P<username>[\w-]+)/$', views.profile, name="profile"),
    path('profile/<str:username>/edit/', views.profile_edit, name="profile_edit"),
]
