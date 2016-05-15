from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from database.models import Song

class DatabaseView(TemplateView):
    template_name = 'site/database.html'

    def get_context_data(self, **kwargs):
        context = super(DatabaseView, self).get_context_data(**kwargs)
        context['songs'] = Song.objects.order_by('title')
        return context

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
