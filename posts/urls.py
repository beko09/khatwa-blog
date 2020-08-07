
from django.urls import path
from .views import (post_home,
                    post_detail, post_create, post_update, post_delete,category_post)
app_name = "posts"
urlpatterns = [
    path('', post_home, name="post_list"),
    path('detail/<str:slug>', post_detail, name="post_detail"),
    path('detail/<str:slug>/edit/', post_update, name="post_update"),
    path('detail/<str:slug>/delete/', post_delete, name="post_delete"),
    path('category/<str:name>/', category_post, name="category"),
    path('create', post_create, name="create"),
    
    
]
