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
    template_name = 'admin/themes.html'

    def get_context_data(self, **kwargs):
        context = super(ThemesView, self).get_context_data(**kwargs)
        context['themes'] = [
            (theme, theme.songs.count())
            for theme in Theme.objects.all()
        ]
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        if action == 'add':
            return self.add_theme()
        elif action == 'edit':
            return self.edit_theme()
        elif action == 'delete':
            return self.delete_theme()
        else:
            return super(ThemesView, self).post(request, *args, **kwargs)

    def add_theme(self):
        name = self.request.POST['name']
        theme = Theme.objects.create(name=name)
        response = {
            'id': theme.id,
            'name': theme.name,
        }
        return JsonResponse(response)

    def edit_theme(self):
        pk = self.request.POST['pk']
        name = self.request.POST['name']

        theme = Theme.objects.get(pk=pk)
        theme.name = name
        theme.save()

        response = {
            'id': theme.id,
            'name': theme.name,
            'songs': theme.songs.count(),
        }
        return JsonResponse(response)

    def delete_theme(self):
        pk = self.request.POST['pk']
        theme = Theme.objects.get(pk=pk)
        id = theme.id
        theme.delete()
        
        response = {
            'id': id,
        }
        return JsonResponse(response)

class AccountView(LoginRequiredMixin, TemplateView):
    pass
