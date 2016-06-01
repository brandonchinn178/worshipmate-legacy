from django.test import TestCase

class WebsiteTest(TestCase):
    def test_all_pages_exist(self):
        for page in ['', 'about', 'contact']:
            response = self.client.get('/%s' % page)
            self.assertNotEqual(response, 500)
