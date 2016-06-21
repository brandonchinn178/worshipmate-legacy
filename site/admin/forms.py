from django import forms
from django.utils.text import slugify
from django.contrib.auth.models import User

from database.models import Song, Theme

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
            'speed': {
                'required': 'Please select the speed of the song',
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

    def save(self):
        instance = super(AddSongForm, self).save(commit=False)
        
        # create a unique slug
        slug = slugify(instance.title)

        if Song.objects.filter(slug=slug).exists():
            # first try adding the artist to the slug
            slug = '%s-%s' % (slug, slugify(instance.artist))
            if Song.objects.filter(slug=slug).exists():
                # then add the primary key which is guaranteed to be unique
                slug = '%s-%d' % (slug, instance.pk)

        instance.slug = slug
        instance.save()
        self.save_m2m()
        
        return instance

class EditSongForm(SongObjectForm):
    class Meta(SongObjectForm.Meta):
        labels = {
            'doc': 'Change .doc file',
            'pdf': 'Change .pdf file',
        }

    def __init__(self, *args, **kwargs):
        super(EditSongForm, self).__init__(*args, **kwargs)

        self.fields['doc'].required = False
        self.fields['pdf'].required = False

class ThemeObjectForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name']
        error_messages = {
            'name': {
                'required': 'Please provide the name of the theme'
            }
        }

    songs = forms.ModelMultipleChoiceField(queryset=Song.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        instance = kwargs['instance']
        if instance is not None:
            kwargs['initial'] = {
                'songs': instance.songs.all()
            }

        super(ThemeObjectForm, self).__init__(*args, **kwargs)

    def save(self):
        theme = super(ThemeObjectForm, self).save()
        songs = self.cleaned_data['songs']
        theme.songs.add(*songs)
        return theme

class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
        ]

    password1 = forms.CharField(label='New password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='New password confirmation', widget=forms.PasswordInput, required=False)

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(
                "The two password fields didn't match",
                code='password_mismatch',
            )

        self.set_password = password1 and password2

    def save(self):
        user = super(AccountForm, self).save(commit=False)
        if self.set_password:
            password = self.cleaned_data['password1']
            user.set_password(password)
        
        user.save()
        return user
