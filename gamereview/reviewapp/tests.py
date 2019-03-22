from django.test import TestCase
from .models import GameType, Game, Review
from .forms import GameForm, ReviewForm
from datetime import datetime
from django.urls import reverse

# Create your tests here.

# Model tests
class TypeTest(TestCase):
    def test_stringOutput(self):
        gametype=GameType(typename='RPG')
        self.assertEqual(str(gametype), gametype.typename)

    def test_tablename(self):
        self.assertEqual(str(GameType._meta.db_table), 'GameType')

class GameTest(TestCase):
    def test_stringOutput(self):
        game=Game(gamename='Kingdom Hearts 3')
        self.assertEqual(str(game), game.gamename)

    def test_tablename(self):
        self.assertEqual(str(Game._meta.db_table), 'Game')

class ReviewTest(TestCase):
    def test_stringOutput(self):
        review=Review(reviewtitle='Ever play an anime?')
        self.assertEqual(str(review), review.reviewtitle)

    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'Review')

# Form invalid tests
class GameFormTest(TestCase):
    def test_gameform_is_invalid(self):
        form = GameForm(data={'gamename': "Dragon Ball FighterZ", 'gametype': "Fighting", 'gamedescription': "A 2D fighting game with familiar anime characters from the Dragon Ball universe."})
        self.assertFalse(form.is_valid())

class ReviewFormTest(TestCase):
    def test_reviewform_is_invalid(self):
        form = ReviewForm(data={'reviewtitle': "KH3: 13 Years Later", 'date': "March 22, 2019"})
        self.assertFalse(form.is_valid())