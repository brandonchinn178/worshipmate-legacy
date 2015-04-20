from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib import messages

import os, string, requests
from database.models import Song, Theme
from main.forms import ContactForm

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

class ContactView(add_title_mixin(FormView)):
    template_name = 'site/contact.html'
    form_class = ContactForm
    title = 'Contact'

    def get(self, request, *args, **kwargs):
        response = super(ContactView, self).get(request, *args, **kwargs)
        response.context_data.update({'title': self.title})
        return response

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        body = form.cleaned_data['message']
        message = "Dear Brandon,\n\n%s\n\nSincerely,\n%s" % (body, name)
        self.send_simple_message(name, email, message)
        messages.success(self.request, 'Thank you! I will respond to your message as soon as I can.')
        return redirect(self.request.path)

    def send_simple_message(self, name, email, message):
        return requests.post(
            "https://api.mailgun.net/v2/worshipdatabase.info/messages",
            auth=("api", os.environ['MAILGUN_KEY']),
            data={"from": name + " <" + email + ">",
                  "to": "Brandon Chinn <brandonchinn178@gmail.com>",
                  "subject": "[Worship Song Database] Contact Form",
                  "text": message})

class SearchView(TitledTemplateView):
    template_name = 'site/search.html'
    title = 'Search'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        query = kwargs['query']
        result = self.search(query)
        context.update(result, query=query)
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
        pages = [
            page for page in (
                'Home', 'About', 'Database', 'Contact', 'Transpose', 'Transposition'
            )
            if page.lower() in query
        ]

        titles = Song.objects.filter(title__search=query)
        artists = Song.objects.filter(artist__search=query).exclude(title__in=titles)
        lyrics = Song.objects.filter(lyrics__search=query).exclude(
            Q(title__in=titles) | Q(artist__in=artists)
        )
        themes = Song.objects.filter(themes__name__search=query)

        return {
            'pages': pages,
            'titles': titles,
            'artists': artists,
            'lyrics': lyrics,
            'themes': themes
        }