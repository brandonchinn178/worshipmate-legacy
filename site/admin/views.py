from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.http.response import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse

from admin.forms import *
from database.models import Song, Theme

def json_error(data):
    return JsonResponse(data, status=500)

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
                return json_error(response)

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

class SongObjectMixin(LoginRequiredMixin, ActionMixin):
    template_name = 'admin/song_object.html'
    model = Song
    actions = {
        'save-song': 'save_song', # AJAX
        'add-theme': 'add_theme',
        'delete': 'delete_song',
    }

    def get_form_kwargs(self):
        kwargs = super(SongObjectMixin, self).get_form_kwargs()
        kwargs['artists'] = Song.objects.order_by('artist').values_list('artist', flat=True).distinct()
        return kwargs

    def save_song(self):
        form = self.get_form()
        if form.is_valid():
            song = form.save()
            return {
                'redirect': song.get_absolute_url(),
            }
        else:
            data = {
                'errors': [
                    message
                    for messages in form.errors.values()
                    for message in messages
                ]
            }
            return json_error(data)

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

class AddSongView(SongObjectMixin, CreateView):
    form_class = AddSongForm

class EditSongView(SongObjectMixin, UpdateView):
    form_class = EditSongForm

    def get_context_data(self, **kwargs):
        context = super(EditSongView, self).get_context_data(**kwargs)
        context['is_edit'] = True
        return context

    def save_song(self):
        self.object = self.get_object()
        return super(EditSongView, self).save_song()

class ThemesView(LoginRequiredMixin, ActionMixin, TemplateView):
    template_name = 'admin/themes.html'
    actions = {
        'delete': 'delete_theme',
    }

    def get_context_data(self, **kwargs):
        context = super(ThemesView, self).get_context_data(**kwargs)
        context['themes'] = [
            (theme, theme.songs.count())
            for theme in Theme.objects.all()
        ]
        return context

    def delete_theme(self):
        pk = self.request.POST['pk']
        theme = Theme.objects.get(pk=pk)
        id = theme.id
        theme.delete()
        
        return {
            'id': id,
        }

class AddThemeView(LoginRequiredMixin, CreateView):
    template_name = 'admin/theme_object.html'
    form_class = ThemeObjectForm

    def form_valid(self, form):
        theme = form.save()
        messages.success(self.request, 'Theme "%s" successfully created' % theme.name)
        return redirect('admin:themes')

class EditThemeView(LoginRequiredMixin, UpdateView):
    template_name = 'admin/theme_object.html'
    form_class = ThemeObjectForm

    def get_object(self):
        name = self.kwargs['name']
        return Theme.objects.get(name=name)

    def get_context_data(self, **kwargs):
        context = super(EditThemeView, self).get_context_data(**kwargs)
        context['is_edit'] = True
        return context

    def form_valid(self, form):
        theme = form.save()
        messages.success(self.request, 'Theme "%s" successfully saved' % theme.name)
        return redirect('admin:themes')

class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/about.html'

class AccountView(LoginRequiredMixin, FormView):
    template_name = 'admin/account.html'
    form_class = AccountForm

    def get_form_kwargs(self):
        kwargs = super(AccountView, self).get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(AccountView, self).get_context_data(**kwargs)
        context['name'] = self.request.user.get_full_name() or self.request.user.username
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Successfully saved account information')
        return redirect(self.request.path)
