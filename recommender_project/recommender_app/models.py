from django.db import models


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    job = models.CharField(max_length=20)
    zipcode = models.IntegerField()


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.CharField(max_length=100)
    video_release = models.CharField(max_length=100)
    imdb_link = models.URLField()


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.CharField(max_length=35)
