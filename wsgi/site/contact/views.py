from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from forms import ContactForm
import requests

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['message']

            context = {
                'name': name,
                'email': email,
                'body': body,
            }
            message = render_to_string('contact/email.txt', context)

            send_simple_message(name, message)
            return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm()

    context = {
        'title': 'Contact',
        'style': 'contact.css',
        'form': form,
    }
    return render(request, 'contact/index.html', context)

def thanks(request):
    context = {'title': 'Thanks'}
    return render(request, 'contact/thanks.html', context)

def send_simple_message(name, message):
    return requests.post(
        "https://api.mailgun.net/v2/worshipdatabase.info/messages",
        auth=("api", "key-946fb135e22d87f1f81c6ccf124ea427"),
        data={"from": "Worship Song Database <no-reply@worshipdatabase.info>",
              "to": "Brandon Chinn <brandonchinn178@gmail.com>",
              "subject": "[Worship Song Database] Contacted by " + name,
              "text": message})