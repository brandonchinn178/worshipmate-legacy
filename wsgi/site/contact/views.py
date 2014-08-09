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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['message']
            recipients = ['brandonchinn178@gmail.com']
            context = {
                'name': name,
                'email': email,
                'body': body,
            }
            message = render_to_string('contact/email.txt', context)
            subject = "Contacted by " + name

            send_mail(subject, message, email, recipients)
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