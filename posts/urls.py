
from django.urls import path
from .views import (
    post_list,  post_detail,
    create_post,  post_update,
    post_delete, category_post,
    like_post,
     )
from django.conf.urls import (
handler400, handler403, handler404, handler500
)
handler404 = 'posts.views.handler404'

app_name = "posts"
urlpatterns = [
    path('', post_list , name = "post_list"),
    path('detail-post/<str:slug>', post_detail , name = "post_detail"),
    path('detail-post/<str:slug>/edit/', post_update, name = "post_update"),
    path('detail-post/<str:slug>/delete/', post_delete, name = "post_delete"),
    path('category/<str:name>/', category_post, name="category"),
    path('create-post', create_post , name = "create"),
    path('like', like_post , name="like"),
    
    
]
