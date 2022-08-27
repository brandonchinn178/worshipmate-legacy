from django.views.generic.base import TemplateView
from django.shortcuts import render

def get_handler(error_code):
    error_templates = {
        404: '404.html',
        500: '500.html',
    }
    return lambda request: render(request, error_templates[error_code])

class AboutView(TemplateView):
    template_name = 'site/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['links'] = [
            ('Dropbox', 'https://www.dropbox.com/sh/c6rryyatkpsnmm8/AADt5uOeBHgHqdvN-1b2ndbYa'),
            ('Facebook', 'https://facebook.com/WorshipMateApp'),
        ]
        return context

class ContactView(TemplateView):
    template_name = 'site/contact.html'
