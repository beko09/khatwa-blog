from django.test import SimpleTestCase
from django.urls import resolve,reverse
from about.views import about,  newsletter_unsubscribe, control_newsletter

class TestUrls(SimpleTestCase):
    
    
    def test_about_urls_resolves(self):
        url = reverse('about:about')
        self.assertEquals(resolve(url).func, about)

    def test_newsletter_unsubscribe_urls_resolves(self):
        url = reverse('about:newsletter_unsubscribe')
        self.assertEquals(resolve(url).func, newsletter_unsubscribe)

    def test_control_newsletter_urls_resolves(self):
        url = reverse('about:control_newsletter')
        self.assertEquals(resolve(url).func, control_newsletter)
