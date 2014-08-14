from django.db import models

# Create your models here.
class Song(models.Model):
    SPEEDS = {
        'F': 'Fast',
        'S': 'Slow',
        'FS': 'Fast/Slow',
    }

    title = models.CharField(max_length=50, primary_key=True)
    artist = models.CharField(max_length=50)
    themes = models.TextField()
    speed = models.CharField(max_length=10, choices=SPEEDS.items())
    lyrics = models.TextField()

    def __unicode__(self):
        return self.title + " | " + self.artist