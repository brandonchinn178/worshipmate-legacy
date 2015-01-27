from django.contrib import admin
from models import Song
import string

class SongFilter(admin.SimpleListFilter):
    title = 'song title'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        letters = tuple('#' + string.ascii_uppercase)
        return (
            zip(letters, letters)
        )

    def queryset(self, request, queryset):
        if self.value() == '#':
            return queryset.filter(title__regex=r'^[0-9]')
        if self.value():
            return queryset.filter(title__istartswith=self.value())

class ArtistFilter(admin.SimpleListFilter):
    title = 'artist'
    parameter_name = 'artist'

    def lookups(self, request, model_admin):
        letters = tuple(string.ascii_uppercase)
        return (
            zip(letters, letters)
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(artist__istartswith=self.value())

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'themes', 'speed')
    list_filter = [SongFilter, ArtistFilter]
    list_per_page = 50
    ordering = ['title']
    prepopulated_fields = {'title_slug': ('title',)}