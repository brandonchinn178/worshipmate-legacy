from django.db import models
from django.utils.text import slugify

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
    doc = models.FileField(upload_to='doc', default='')
    pdf = models.FileField(upload_to='pdf', default='')

    def __unicode__(self):
        return "%s | %s" % (self.title, self.artist)

    @models.permalink
    def get_absolute_url(self):
        if not self.title_slug:
            # set title_slug if not already set
            self.title_slug = slugify(unicode(self.title))

        return ('song', (), {'title': self.title_slug})

class Theme(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __unicode__(self):
        return self.name