from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.utils.html import format_html_join

from database.models import Song

class DatabaseView(TemplateView):
    template_name = 'site/database.html'

    def get_context_data(self, **kwargs):
        context = super(DatabaseView, self).get_context_data(**kwargs)
        context['songs'] = [
            (song, self.format_themes(song))
            for song in Song.objects.order_by('title')
        ]
        return context

    def format_themes(self, song):
        return format_html_join(
            ', ',
            '<a href="#">{}</a>',
            ([theme] for theme in song.themes.all()),
        )

class SongView(DetailView):
    template_name = 'site/song.html'
    model = Song
    slug_field = 'title_slug'
    slug_url_kwarg = 'title'
    context_object_name = 'song'
