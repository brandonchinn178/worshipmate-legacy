from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db.models import Q

import os, string
from database.models import Song

def add_title_mixin(view_class):
    """
    Generates a class that extends the given class to include a class variable 'title'
    that will be in the context data
    """
    class TitledView(view_class):
        title = ''

        def get_context_data(self, **kwargs):
            context = super(TitledView, self).get_context_data(**kwargs)
            context['title'] = self.title
            return context

        def get(self, request, *args, **kwargs):
            """ In case the parent view (i.e. FormView) doesn't use get_context_data """
            response = super(TitledView, self).get(request, *args, **kwargs)
            response.context_data.update({'title': self.title})
            return response

    return TitledView

TitledTemplateView = add_title_mixin(TemplateView)

class HomeView(TitledTemplateView):
    template_name = 'site/index.html'
    title = 'Home'

class AboutView(TitledTemplateView):
    template_name = 'site/about.html'
    title = 'About'

class TransposeView(TitledTemplateView):
    template_name = 'site/transpose.html'
    title = 'Transpose'

class SearchView(TitledTemplateView):
    template_name = 'site/search.html'
    title = 'Search'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        query = kwargs['query']
        result = self.search(query)
        context.update({
            'query': query,
            'pages': result['pages'],
            'songs': result['songs']
        })
        return context

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        if query == '':
            return redirect('home')
        kwargs.update({'query': query})
        return super(SearchView, self).get(request, *args, **kwargs)

    def search(self, query):
        """
        Searches website pages and database songs for the given query
        """
        # search pages
        pages = []
        for page, link in {
                ('Home', 'home'),
                ('About', 'about'),
                ('Database', 'database:index'),
                ('Contact', 'contact:index'),
                ('Transpose', 'transpose:index'),
                ('Transposition', 'transpose:index')
            }:
            if page.lower() in query:
                pages.append((page, reverse(link)))

        # search songs
        songs = Song.objects.filter(
            Q(title__search=query) |
            Q(artist__search=query) |
            Q(themes__search=query) |
            Q(lyrics__search=query)
        )

        return {
            'pages': pages,
            'songs': songs
        }