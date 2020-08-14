from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('profile/<str:username>/', views.profile, name="profile"),
    # re_path(r'^profile/(?P<username>[\w-]+)/$', views.profile, name="profile"),
    path('profile/<str:username>/edit/', views.profile_edit, name="profile_edit"),
    path('password_reset_confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
     name='password_reset_confirm'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
]
