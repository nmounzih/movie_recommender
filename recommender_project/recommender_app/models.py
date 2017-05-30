from django.db import models
from django.contrib.auth.models import User


class Rater(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    job = models.CharField(max_length=20)
    zipcode = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    video_release = models.CharField(max_length=100)
    imdb_link = models.URLField()


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.DateTimeField()
