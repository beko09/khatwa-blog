from django.test import SimpleTestCase
from django.urls import resolve,reverse
from comments.views import comment_thread,  comment_delete

class TestUrls(SimpleTestCase):
    
    
    

    def test_thread_comment_urls_resolves(self):
        url = reverse('comments:thread', args=[20])
        self.assertEquals(resolve(url).func, comment_thread)
    def test_comment_delete_urls_resolves(self):
        url = reverse('comments:comment_delete', args=[20])
        self.assertEquals(resolve(url).func, comment_delete)

   