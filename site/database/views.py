from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from database.models import Song
from main.views import add_title_mixin

class DatabaseView(add_title_mixin(ListView)):
    template_name = 'site/database.html'
    model = Song
    queryset = Song.objects.order_by('title')
    title = 'Database'
    context_object_name = 'songs'

class SongView(DetailView):
    template_name = 'site/song.html'
    model = Song
    slug_field = 'title_slug'
    slug_url_kwarg = 'title'
    context_object_name = 'song'

    def get_context_data(self, **kwargs):
        context = super(SongView, self).get_context_data(**kwargs)
        less = Song.objects.filter(title__lt=self.object.title).order_by('title').reverse()
        greater = Song.objects.filter(title__gt=self.object.title).order_by('title')
        if less.count() != 0:
            context['before'] = less[0]
        if greater.count() != 0:
            context['after'] = greater[0]
        context['title'] = self.object.title
        return context
