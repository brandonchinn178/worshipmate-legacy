from django.test import TestCase
from django.test.client import RequestFactory
from django.views.generic.base import View, TemplateView
from django.db import connection

from main.views import add_title_mixin, SearchView
from database.models import Song

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
        setattr(TestView, 'template_name', 'foo.html')
        view = TestView.as_view()
        request = self.factory.get('/')
        response = view(request)
        self.assertEqual(response.context_data['title'], 'Test Title')

    def test_add_title_mixin_with_generic_view(self):
        """
        Some View classes don't use get_context_data, so we have to make sure it also
        works on a generic get request
        """
        class NewView(View):
            def get(self, request, *args, **kwargs):
                response = self.options(request)
                setattr(response, 'context_data', {})
                return response

        TestView = add_title_mixin(NewView)
        setattr(TestView, 'title', 'Hello')
        view = TestView.as_view()
        request = self.factory.get('/')
        response = view(request)
        self.assertEqual(response.context_data['title'], 'Hello')

# class SearchTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         c = connection.cursor()
#         c.execute("ALTER TABLE database_song ADD COLUMN FTS_DOC_ID BIGINT UNSIGNED NOT NULL")
#         c.execute("ALTER TABLE database_song ADD KEY (FTS_DOC_ID)")
#         c.execute("ALTER TABLE database_song CHANGE FTS_DOC_ID FTS_DOC_ID BIGINT UNSIGNED NOT NULL AUTO_INCREMENT")
#         c.execute("ALTER TABLE database_song ADD FULLTEXT KEY (title)")
#         c.execute("ALTER TABLE database_song ADD FULLTEXT KEY (artist)")
#         c.execute("ALTER TABLE database_song ADD FULLTEXT KEY (lyrics)")

#         c.execute("ALTER TABLE database_theme ADD COLUMN FTS_DOC_ID BIGINT UNSIGNED NOT NULL")
#         c.execute("ALTER TABLE database_theme ADD KEY (FTS_DOC_ID)")
#         c.execute("ALTER TABLE database_theme CHANGE FTS_DOC_ID FTS_DOC_ID BIGINT UNSIGNED NOT NULL AUTO_INCREMENT")
#         c.execute("ALTER TABLE database_theme ADD FULLTEXT KEY (name)")

#     def tearDown(self):
#         c = connection.cursor()
#         c.execute("ALTER TABLE database_song DROP COLUMN FTS_DOC_ID")
#         c.execute("ALTER TABLE database_theme DROP COLUMN FTS_DOC_ID")

#     def test_search(self):
#         view = SearchView()
#         song_a = Song.objects.create(title='alpha', artist='test')
#         song_b = Song.objects.create(title='beta', artist='test')
#         search = view.search('alpha')
#         self.assertIn(song_a, search['songs'])
#         self.assertNotIn(song_b, search['songs'])
#         self.assertEqual(search['pages'], [])

#     def test_search_page(self):
#         view = SearchView()
#         for page in ['home', 'about', 'contact', 'database', 'transpose']:
#             search = view.search(page)
#             self.assertNotEqual(search['pages'], [])
#             self.assertEqual(search['pages'][0][0].lower(), page)

#     def test_redirect(self):
#         view = SearchView.as_view()
#         request = self.factory.get('/')
#         response = view(request)
#         self.assertEqual(response.status_code, 302)

#         request = self.factory.get('/?foo=bar')
#         response = view(request)
#         self.assertEqual(response.status_code, 302)

#         request = self.factory.get('/?query=hi')
#         response = view(request)
#         self.assertEqual(response.status_code, 200)