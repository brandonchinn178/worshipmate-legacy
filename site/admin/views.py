from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from database.models import Song, Theme

class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['songs'] = Song.objects.order_by('title')
        return context

class AddSongView(LoginRequiredMixin, TemplateView):
    pass

class EditSongView(LoginRequiredMixin, TemplateView):
    pass

class AccountView(LoginRequiredMixin, TemplateView):
    pass
