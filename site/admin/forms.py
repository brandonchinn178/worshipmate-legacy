from django import forms
from django.utils.text import slugify

from database.models import Song

class SongObjectForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            'title',
            'artist',
            'lyrics',
            'themes',
            'speed',
            'doc',
            'pdf',
        ]
        error_messages = {
            'title': {
                'required': 'Please provide the title of the song',
            },
            'artist': {
                'required': 'Please provide the artist of the song',
            },
            'lyrics': {
                'required': 'Please provide the lyrics of the song',
            },
            'themes': {
                'required': 'Please provide the themes for the song',
            },
            'doc': {
                'required': 'No .doc file submitted',
            },
            'pdf': {
                'required': 'No .pdf file submitted',
            },
        }

    def __init__(self, *args, **kwargs):
        super(SongObjectForm, self).__init__(*args, **kwargs)

        # remove label suffix
        for field in ['lyrics', 'themes', 'doc', 'pdf']:
            self.fields[field].label_suffix = ''

class AddSongForm(SongObjectForm):
    class Meta(SongObjectForm.Meta):
        labels = {
            'doc': 'Upload .doc file',
            'pdf': 'Upload .pdf file',
        }

    def save(self, commit=True):
        instance = super(AddSongForm, self).save(commit=commit)
        
        # create a unique slug
        slug = slugify(instance.title)

        if Song.objects.filter(title_slug=slug).exists():
            # first try adding the artist to the slug
            slug = '%s-%s' % (slug, slugify(instance.artist))
            if Song.objects.filter(title_slug=slug).exists():
                # then add the primary key which is guaranteed to be unique
                slug = '%s-%d' % (slug, instance.pk)

        instance.title_slug = slug
        instance.save()
        
        return instance

class EditSongForm(SongObjectForm):
    def __init__(self, *args, **kwargs):
        super(EditSongForm, self).__init__(*args, **kwargs)

        self.fields['doc'].required = False
        self.fields['pdf'].required = False
