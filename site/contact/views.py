from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import ContactForm
from mailgun import send_simple_message

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['message']
            
            message = "Dear Brandon,\n\n" + body + "\n\nSincerely,\n" + name

            send_simple_message(name, email, message)
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
