from django.test import SimpleTestCase
from django.urls import resolve,reverse
from posts.views import (
    post_list,  post_detail,
    create_post,  post_update,
    post_delete,  category_post
     )

class TestUrls(SimpleTestCase):
    
    
    def test_create_post_urls_resolves(self):
        url = reverse('posts:create')
        self.assertEquals(resolve(url).func, create_post)

    def test_list_post_urls_resolves(self):
        url = reverse('posts:post_list')
        self.assertEquals(resolve(url).func, post_list)

    def test_detail_post_urls_resolves(self):
        url = reverse('posts:post_detail', args=['test'])
        self.assertEquals(resolve(url).func, post_detail)

    def test_update_post_urls_resolves(self):
        url = reverse('posts:post_update', args=['test'])
        self.assertEquals(resolve(url).func, post_update)

    def test_delete_post_urls_resolves(self):
        url = reverse('posts:post_delete', args=['test'])
        self.assertEquals(resolve(url).func, post_delete)