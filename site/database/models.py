from django.db import models
from django.core.exceptions import ValidationError

import os

def validate_file(filename, ext):
    """
    Validates the extension of a file
    """
    filename = value.name
    extension = os.path.splitext(filename)[1]
    if extension != ext:
        print extension, ext
        raise ValidationError('Invalid file extension: %s' % filename, code='invalid_ext')

def doc_file_validator(filename):
    return validate_file(filename, '.doc')

def pdf_file_validator(filename):
    return validate_file(filename, '.pdf')

class Song(models.Model):
    SPEEDS = (
        ('F', 'Fast'),
        ('S', 'Slow'),
        ('FS', 'Fast/Slow'),
    )

    title = models.CharField(max_length=100)
    title_slug = models.SlugField()
    artist = models.CharField(max_length=50)
    themes = models.ManyToManyField('Theme')
    speed = models.CharField(max_length=2, choices=SPEEDS)
    lyrics = models.TextField()
    doc = models.FileField(upload_to='doc', validators=[doc_file_validator])
    pdf = models.FileField(upload_to='pdf', validators=[pdf_file_validator])

    def __unicode__(self):
        return "%s | %s" % (self.title, self.artist)

    @models.permalink
    def get_absolute_url(self):
        return ('song', (), {'slug': self.title_slug})

class Theme(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name