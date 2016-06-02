from django.test import TestCase
from django.db.utils import IntegrityError

from database.models import Song

class SongTest(TestCase):
    def test_no_title(self):
        """Every song MUST have a title"""
        self.assertRaises(
            IntegrityError,
            Song.objects.create
        )