from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail

import os, string
from database.models import Song, Theme
from main.forms import ContactForm

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
            ('Dropbox', '#'),
            ('Facebook', 'http://facebook.com/WorshipSongDatabase'),
            ('My SoundCloud', 'http://soundcloud.com/brandonchinn178'),
            ('My Website', 'http://brandonchinn178.github.io'),
        ]
        return context

class ContactView(FormView):
    template_name = 'site/contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['success'] = 'success' in self.request.GET
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        body = form.cleaned_data['message']
        message = "Dear Brandon,\n\n%s\n\nSincerely,\n%s" % (body, name)
        self.send_simple_message(name, email, message)
        return redirect('%s?success' % self.request.path)

    def send_simple_message(self, name, email, message):
        send_mail(
            '[Worship Song Database] Contact Form',
            message,
            '%s <%s>' % (name, email),
            ['Brandon Chinn <brandonchinn178@gmail.com>'],
        )
