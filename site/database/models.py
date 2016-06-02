from django.db import models
from django.core.exceptions import ValidationError

import os

def validate_file(value, ext):
    """
    Validates the extension of a file
    """
    filename = value.name
    extension = os.path.splitext(filename)[1]
    if extension != ext:
        raise ValidationError('Invalid file extension: %s' % filename, code='invalid_ext')

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
    slug = models.SlugField()
    artist = models.CharField(max_length=50)
    themes = models.ManyToManyField('Theme')
    speed = models.CharField(max_length=2, choices=SPEEDS)
    lyrics = models.TextField()
    doc = models.FileField(upload_to=doc_upload_file, validators=[doc_file_validator])
    pdf = models.FileField(upload_to=pdf_upload_file, validators=[pdf_file_validator])

    def __unicode__(self):
        return "%s | %s" % (self.title, self.artist)

    @models.permalink
    def get_absolute_url(self):
        return ('song', (), {'slug': self.slug})

class Theme(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name