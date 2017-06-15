from rest_framework import serializers
from .models import Rater, Movie, Rating


class RaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rater
        fields = ('id', 'age', 'gender', 'job', 'zipcode')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'release_year', 'video_release', 'imdb_link')


class RatingSerializer(serializers.ModelSerializer):
    model = Rating
    class Meta:
        model = ('rater', 'movie', 'rating', 'timestamp')
