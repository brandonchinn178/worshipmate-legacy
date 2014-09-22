from django.shortcuts import render, get_object_or_404
from models import Song

# Create your views here.
def index(request):
    songs = Song.objects.order_by('title')
    context = {
        'title': 'Database',
        'style': 'database.css',
        'script': 'database.js',
        'songs': songs
    }
    return render(request, 'database/index.html', context)

def detail(request, title):
    title = title.replace("-", " ");
    song = get_object_or_404(Song, title=title)
    before = Song.objects.filter(title__lt=song.title).order_by('title').reverse()
    after = Song.objects.filter(title__gt=song.title)
    context = {
        'title': song.title,
        'style': 'database.css',
        'song': song,
        'navigate': {'before': before, 'after': after}
    }
    return render(request, 'database/detail.html', context)