from django.test import SimpleTestCase
from django.urls import resolve,reverse
from accounts.views import  register,  profile, profile_edit

class TestUrls(SimpleTestCase):
    
    
    def test_register_urls_resolves(self):
        url = reverse('accounts:register')
        self.assertEquals(resolve(url).func, register)

    def test_profile_urls_resolves(self):
        url = reverse('accounts:profile', args=['beko09'])
        self.assertEquals(resolve(url).func, profile)

    def test_profile_edit_urls_resolves(self):
        url = reverse('accounts:profile_edit', args=['beko09'])
        self.assertEquals(resolve(url).func, profile_edit)

  