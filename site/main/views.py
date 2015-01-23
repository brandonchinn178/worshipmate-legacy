from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q

import os, string
from database.models import Song

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

    context = {
        'title': 'Search',
        'style': 'search.css',
        'query': query,
        'pages': result['pages'],
        'songs': result['songs']
    }
    return render(request, 'main/search.html', context)

def doSearch(query):
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