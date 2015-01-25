from django.test import TestCase
from django.test.client import RequestFactory()
from django.views.generic.base import TemplateView

from main.views import add_title_mixin

class WebsiteTest(TestCase):
    def test_all_pages_exist(self):
        for page in ['', 'about', 'contact', 'database', 'transpose']:
            response = self.client.get('/%s' % page)
            self.assertNotEqual(response, 500)

class ViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_title_mixin(self):
        TestView = add_title_mixin(TemplateView)
        setattr(TestView, 'title', 'Test Title')
        view = TestView.as_view()
        request = self.factory.get('/')
        response = view(request)
        self.assertEqual(response.context_data['title'], 'Test Title')