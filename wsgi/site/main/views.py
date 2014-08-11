from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'style': 'home.css'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {'title': 'About'}
    return render(request, 'main/about.html', context)

def search(request):
    params = request.GET
    if len(params) == 0:
        return HttpResponseRedirect(reverse('home'))
    query = params['query']
    result = doSearch(query)
    pages = result['pages']
    titles = result['titles']
    lyrics = result['lyrics']

    context = {
        'title': 'Search',
        'pages': pages,
        'titles': titles,
        'lyrics': lyrics
    }

    return render(request, 'main/search.html', context)

def doSearch(query):
    return {
        'pages': [],
        'titles': [],
        'lyrics': []
    }