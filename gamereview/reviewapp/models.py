from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# GameType, Game, Review

class GameType(models.Model):
    typename = models.CharField(max_length=255)
    typedescription = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table = 'GameType'

class Game(models.Model):
    gamename = models.CharField(max_length=255)
    gametype = models.ForeignKey(GameType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    gameentrydate = models.DateField()
    gameurl = models.URLField(null =True, blank=True)
    gamedescription = models.TextField()

    def __str__(self):
        return self.gamename

    class Meta:
        db_table = 'Game'

class Review(models.Model):
    reviewtitle = models.CharField(max_length=255)
    reviewdate = models.DateField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    rating = models.SmallIntegerField()
    revuewtext = models.TextField()

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table = 'Review'