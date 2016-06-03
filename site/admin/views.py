from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.http.response import HttpResponse, JsonResponse

from admin.forms import *
from database.models import Song, Theme

class ActionMixin(object):
    """
    Allows views to specify actions to take if "action" is present
    in the POST data
    """
    # maps action value to name of function
    actions = {}

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        if action in self.actions:
            func = self.actions[action]
            try:
                response = getattr(self, func)()
            except Exception as e:
                response = {
                    'message': e.message,
                }
                return JsonResponse(response, status=500)

            if isinstance(response, HttpResponse):
                return response
            else:
                return JsonResponse(response)
        else:
            return super(ActionMixin, self).post(request, *args, **kwargs)

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

class EditSongView(LoginRequiredMixin, ActionMixin, UpdateView):
    template_name = 'admin/song_object.html'
    model = Song
    form_class = EditSongForm
    actions = {
        'delete': 'delete_song',
        'add-theme': 'add_theme',
    }

    def get_context_data(self, **kwargs):
        context = super(EditSongView, self).get_context_data(**kwargs)
        context['is_edit'] = True
        return context

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
        theme = Theme.objects.create_from_post(self.request.POST)
        return {
            'id': theme.id,
            'name': theme.name,
        }

class ThemesView(LoginRequiredMixin, ActionMixin, TemplateView):
    template_name = 'admin/themes.html'
    actions = {
        'add': 'add_theme',
        'edit': 'edit_theme',
        'delete': 'delete_theme',
    }

    def get_context_data(self, **kwargs):
        context = super(ThemesView, self).get_context_data(**kwargs)
        context['themes'] = [
            (theme, theme.songs.count())
            for theme in Theme.objects.all()
        ]
        return context

    def add_theme(self):
        theme = Theme.objects.create_from_post(self.request.POST)
        return {
            'id': theme.id,
            'name': theme.name,
        }

    def edit_theme(self):
        theme = Theme.objects.update_from_post(self.request.POST)
        return {
            'id': theme.id,
            'name': theme.name,
            'songs': theme.songs.count(),
        }

    def delete_theme(self):
        pk = self.request.POST['pk']
        theme = Theme.objects.get(pk=pk)
        id = theme.id
        theme.delete()
        
        return {
            'id': id,
        }

class AccountView(LoginRequiredMixin, TemplateView):
    pass
