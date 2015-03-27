from django.contrib import admin
from database.models import Song, Theme
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
    class Media:
        css = {
            'all': (
                'style/vendor/select2.css',
                'style/vendor/select2-spinner.gif',
                'style/vendor/select2.png',
            )
        }
        js = (
            'scripts/vendor/jquery.min.js',
            'scripts/vendor/select2.min.js',
            'scripts/admin_song.js',
        )

    list_display = ('title', 'artist', 'get_themes', 'speed')
    list_filter = [SongFilter, ArtistFilter]
    list_per_page = 50
    ordering = ['title']
    prepopulated_fields = {'title_slug': ('title',)}

    def get_themes(self, obj):
        return ", ".join([theme.name for theme in obj.themes.all()])
    get_themes.short_description = 'Themes'

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 50
    ordering = ['name']