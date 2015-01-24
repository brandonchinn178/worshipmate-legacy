from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib import messages

from contact.forms import ContactForm
from main.views import add_title_mixin

import requests, os

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
