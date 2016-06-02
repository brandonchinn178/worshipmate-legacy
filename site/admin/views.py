from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect

from admin.forms import *
from database.models import Song

class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['songs'] = Song.objects.order_by('title')
        return context

class AddSongView(LoginRequiredMixin, CreateView):
    template_name = 'admin/song_object.html'
    form_class = AddSongForm

    def form_valid(self, form):
        song = form.save()
        messages.success(self.request, 'Song "%s" successfully created' % song.title)
        return redirect('admin:index')

class EditSongView(LoginRequiredMixin, UpdateView):
    template_name = 'admin/song_object.html'
    model = Song
    slug_field = 'title_slug'
    form_class = EditSongForm

    def get_context_data(self, **kwargs):
        context = super(EditSongView, self).get_context_data(**kwargs)
        context['is_edit'] = True
        return context

    def post(self, request, *args, **kwargs):
        return super(EditSongView, self).post(request, *args, **kwargs)

class AccountView(LoginRequiredMixin, TemplateView):
    pass
