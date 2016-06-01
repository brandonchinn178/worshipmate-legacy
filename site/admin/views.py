from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from database.models import Song, Theme

class MainView(LoginRequiredMixin, TemplateView):
    pass
