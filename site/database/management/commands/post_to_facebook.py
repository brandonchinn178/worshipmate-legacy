from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.template.loader import render_to_string
from django.conf import settings

import facebook, os

from database.models import Song

access_token = os.environ.get('FACEBOOK_ACCESS_TOKEN')

class Command(BaseCommand):
    help = 'Post unposted songs to Facebook'

    def handle(self, *args, **options):
        songs = Song.objects.filter(post_facebook=False)

        if songs.count() == 0:
            print 'No songs to post!'
            return
        elif songs.count() == 1:
            context = {
                'song': song,
            }
            message = '"%s" by %s has been added to the database!' % (song.title, song.artist)
            self.post_facebook(message)
        else:
            song_list = ', '.join([
                '%s (%s)' % (song.title, song.artist)
                for i, song in enumerate(songs)
                if i != songs.count() - 1
            ])
            if len(song_list) > 1:
                song_list += ','
            last_song = songs.last()
            message = '%s and %s (%s) have been added to the database!' % (
                song_list,
                last_song.title,
                last_song.artist,
            )
            self.post_facebook(message)

        songs.update(post_facebook=True)

    def post_facebook(self, message):
        print 'Posting to Facebook: %s' % message
        graph = facebook.GraphAPI(access_token=access_token)
        try:
            graph.put_object('me', 'feed', message=message)
        except Exception as e:
            import logging
            logging.error('An error occurred when posting to Facebook: %s' % e)
            logging.debug('The message: %s' % message)
            raise e # re-raise exception to alert user something went wrong
