from django.db import models, IntegrityError
from django.core.exceptions import ValidationError

import os

def validate_file(value, ext):
    """
    Validates the extension of a file
    """
    filename = value.name
    extension = os.path.splitext(filename)[1]
    if extension != ext:
        raise ValidationError('Invalid file extension for %s: %s' % (ext, filename), code='invalid_ext')

def upload_file(song, filename, ext):
    """
    Songs saved as <subdir>/<slug>.<ext>
    """
    return '%s/%s.%s' % (
        ext, song.slug, ext
    )

def doc_file_validator(value):
    return validate_file(value, '.doc')

def doc_upload_file(song, filename):
    return upload_file(song, filename, 'doc')

def pdf_file_validator(value):
    return validate_file(value, '.pdf')

def pdf_upload_file(song, filename):
    return upload_file(song, filename, 'pdf')

class Song(models.Model):
    SPEEDS = (
        ('', ''),
        ('F', 'Fast'),
        ('S', 'Slow'),
        ('FS', 'Fast/Slow'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    artist = models.CharField(max_length=50)
    themes = models.ManyToManyField('Theme', related_name='songs')
    speed = models.CharField(max_length=2, choices=SPEEDS)
    lyrics = models.TextField()
    doc = models.FileField(upload_to=doc_upload_file, validators=[doc_file_validator])
    pdf = models.FileField(upload_to=pdf_upload_file, validators=[pdf_file_validator])

    def __unicode__(self):
        return "%s | %s" % (self.title, self.artist)

    @models.permalink
    def get_absolute_url(self):
        return ('song', (), {'slug': self.slug})

class ThemeManager(models.Manager):
    def create_from_post(self, data):
        name = data['name']
        if name == '':
            raise ValidationError('No name provided')

        try:
            return self.create(name=name)
        except IntegrityError:
            raise ValidationError('Theme "%s" already exists' % name)

class Theme(models.Model):
    class Meta:
        ordering = ['name']

    objects = ThemeManager()
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name
