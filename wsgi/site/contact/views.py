from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from forms import ContactForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            context = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'body': form.cleaned_data['message'],
            }
            message = render_to_string('contact/email.txt', context)

            recipients = ['brandonchinn178@gmail.com']
            subject = "Contacted by " + name
            sender = "Worship Song Database <no-reply@worshipdatabase.info>"

            send_mail(subject, message, sender, recipients)
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