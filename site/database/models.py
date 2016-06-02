from django.db import models
from django.core.exceptions import ValidationError

import os

def get_file_validator(ext):
    """
    Validates the extension of a file
    """
    def file_validator(value):
        filename = value.name
        extension = os.path.splitext(filename)[1]
        if extension != ext:
            print extension, ext
            raise ValidationError('Invalid file extension: %s' % filename, code='invalid_ext')
    return file_validator

doc_file_validator = get_file_validator('.doc')
pdf_file_validator = get_file_validator('.pdf')

class Song(models.Model):
    SPEEDS = {
        'F': 'Fast',
        'S': 'Slow',
        'FS': 'Fast/Slow',
    }

    title = models.CharField(max_length=50, primary_key=True, default=None)
    title_slug = models.SlugField(default='')
    artist = models.CharField(max_length=50, default='')
    themes = models.ManyToManyField('Theme')
    speed = models.CharField(max_length=10, choices=SPEEDS.items(), default='')
    lyrics = models.TextField(null=True, blank=True)
    doc = models.FileField(upload_to='doc', default='', validators=[doc_file_validator])
    pdf = models.FileField(upload_to='pdf', default='', validators=[pdf_file_validator])

    def __unicode__(self):
        return "%s | %s" % (self.title, self.artist)

    @models.permalink
    def get_absolute_url(self):
        return ('song', (), {'slug': self.title_slug})

class Theme(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __unicode__(self):
        return self.name