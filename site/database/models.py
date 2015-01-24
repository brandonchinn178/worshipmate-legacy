from django.db import models

class Song(models.Model):
    SPEEDS = {
        'F': 'Fast',
        'S': 'Slow',
        'FS': 'Fast/Slow',
    }

    title = models.CharField(max_length=50, primary_key=True)
    title_slug = models.SlugField(default='')
    artist = models.CharField(max_length=50, null=True)
    themes = models.TextField(null=True)
    speed = models.CharField(max_length=10, choices=SPEEDS.items(), null=True)
    lyrics = models.TextField(null=True)
    doc = models.FileField(upload_to='doc', default='')
    pdf = models.FileField(upload_to='pdf', default='')

    def __unicode__(self):
        return self.title + " | " + self.artist

    @models.permalink
    def get_absolute_url(self):
        return ('song', (), {'title': self.title_slug})