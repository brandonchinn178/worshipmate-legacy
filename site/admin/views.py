from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.http.response import JsonResponse

from admin.forms import *
from database.models import Song, Theme

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
    form_class = EditSongForm

    def get_context_data(self, **kwargs):
        context = super(EditSongView, self).get_context_data(**kwargs)
        context['is_edit'] = True
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        if action == 'delete':
            return self.delete_song()
        elif action == 'add-theme':
            return self.add_theme()
        else:
            return super(EditSongView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        song = form.save()
        messages.success(self.request, 'Song "%s" successfully saved' % song.title)
        return redirect('admin:index')

    def delete_song(self):
        song = self.get_object()
        song.delete()
        messages.success(self.request, 'Song "%s" successfully deleted' % song.title)
        return redirect('admin:index')

    def add_theme(self):
        name = self.request.POST['name']
        theme = Theme.objects.create(name=name)
        response = {
            'id': theme.id,
            'name': theme.name,
        }
        return JsonResponse(response)

class ThemesView(LoginRequiredMixin, TemplateView):
    # TODO: add/edit themes here
    pass

class AccountView(LoginRequiredMixin, TemplateView):
    pass
