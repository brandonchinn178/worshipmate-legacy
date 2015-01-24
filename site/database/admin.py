from django.contrib import admin
from models import Song

class SongFilter(admin.SimpleListFilter):
    title = 'song title'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        letters = tuple(list('#ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        return (
            zip(letters, letters)
        )

    def queryset(self, request, queryset):
        if self.value() == '#':
            return queryset.filter(title__regex=r'^[0-9]')
        if self.value():
            return queryset.filter(title__istartswith=self.value())

class SpeedFilter(admin.SimpleListFilter):
    title = 'speed'
    parameter_name = 'speed'

    def lookups(self, request, model_admin):
        return (
            ('f', 'Fast'),
            ('s', 'Slow'),
            ('fs', 'Fast/Slow'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'f':
            return queryset.filter(speed='F')
        if self.value() == 's':
            return queryset.filter(speed='S')
        if self.value() == 'fs':
            return queryset.filter(speed='FS')

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'themes', 'speed')
    list_filter = [SongFilter, SpeedFilter]
    list_per_page = 50
    ordering = ['title']
    prepopulated_fields = {'title_slug': ('title',)}

admin.site.register(Song, SongAdmin)